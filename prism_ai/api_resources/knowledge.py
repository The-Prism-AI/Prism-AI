from prism_ai.api_resources.api_resource import APIResource
import requests
from tqdm import tqdm
import os
import pathlib
import httpx
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

supported_file_types = [
    "pdf",
    "doc",
    "docx",
    "txt",
    "md",
    "odt",
    "gz"
]

# async def async_post(url, data, headers):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(url, data=data, headers=headers)
#     return response

class Knowledge(APIResource):

    '''
    Knowledge Object to be created
    '''
    
    @classmethod
    def create(
        cls,
        **params,
    ):
            
        '''
        Create a new Knowledge Object from a url
        '''

        method = params.pop("method", None)
        name = params.pop("name", None)
        kb_id = params.pop("kb_id", None)
        source = params.pop("source", None)

        class FileWithProgress:
            def __init__(self, file, total_size, chunk_size=1024*1024):
                self.file = file
                self.total_size = total_size
                self.chunk_size = chunk_size
                self.read_size = 0

            def __iter__(self):
                return self

            def __next__(self):
                data = self.file.read(self.chunk_size)
                if not data:
                    raise StopIteration
                self.read_size += len(data)
                progress_bar.update(len(data))
                return data

        if None in [name, kb_id, source]:
                
            cls._no_params_message(
                
                endpoint="Knowledge",
                req_pars=[
                    "name",
                    "kb_id",
                    "source",
                ],
            )
            return None
        
        if method == "text":
            return cls._post(
                endpoint_url=f"users/knowledge_base/{kb_id}/knowledge_from_text/",
                name=name,
                text=source,
                **params,
            )

        elif method == "url":
            return cls._post(
                endpoint_url=f"users/knowledge_base/{kb_id}/knowledge_from_url/",
                name=name,
                url=source,
                **params,
            )
            
        elif method == "file":

            try:
                dir_path = pathlib.Path(source)
            except: 
                raise ValueError("The path you provided is not valid.")

            if dir_path.is_dir(): # We're dealing with a directory.

                print("You've provided a directory, to the Knowledge.create method.\n\nPlease use the KnowledgeBase.create method to create a KnowledgeBase from a directory, to create multiple knowledge objects from a directory.")

            else: # We're dealing with a file. 

                instance = cls(endpoint_url="upload/")
                file_size = os.path.getsize(source)

                info_instance = instance._get(endpoint_url="basic_user_info/", quiet=True)
                user_info = info_instance.json

                if user_info["max_storage"] != None:
                    if file_size / (1024 * 1024) > user_info["max_storage"]:
                        raise ValueError("You have exceeded your storage limit. Please upgrade your plan to continue using prism.")
                else: 
                    pass
                if user_info["tokens_remaining"] <= 0:
                    raise ValueError("You have no tokens remaining. Please upgrade your plan to continue using prism.")
                if file_size > 4 * 1024 * 1024 * 1024:
                    raise ValueError("The file you provided is too large. The maximum file size is 4GB.")
                if str(source).split(".")[-1] not in supported_file_types:
                    raise ValueError("The file you provided is not supported. \nSupported file types are: \n\n - pdf \n - doc \n - docx \n - txt \n - md \n - odt")

                with open(source, 'rb') as file:
                    
                    unique_name = "kb_"+str(kb_id)+"/"+name
                    print("Uploading file "+str(source)+" as "+str(name)+" ...")

                    file_like = FileWithProgress(file, file_size)

                    headers = instance.create_headers(kb_id=kb_id, unique_name=unique_name)
                    url = instance.api_url + "upload/"

                    with requests.Session() as session: 
                        with tqdm(total=file_size, unit='B', unit_scale=True, dynamic_ncols=True) as progress_bar:
                            response = session.post(url, data=file_like, headers=headers)
                        # k_id = response.json()["id"]
                    
                    return response
                    # return cls._get(
                    #     endpoint_url=f"knowledge/{k_id}/",
                    # )
                    # return cls._post(
                    #     endpoint_url=f"users/knowledge_base/{kb_id}/knowledge_from_file/",
                    #     name=name,
                    #     s3_bucket=unique_name,
                    #     **params
                    # )

                return {}

