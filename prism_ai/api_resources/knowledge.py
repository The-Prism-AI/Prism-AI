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

class Knowledge(APIResource):

    '''
    Knowledge Object to be created
    '''
    
    @classmethod
    def create(
        cls,
        method: str,
        name: str, 
        kb_id: int,
        source: str,
        **params,
    ):
            
        '''
        Create a new Knowledge Object from a url
        '''

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

            if dir_path.is_dir():

                print("You've provided a directory, to the Knowledge.create method.\n\nPlease use the KnowledgeBase.create method to create a KnowledgeBase from a directory, to create multiple knowledge objects from a directory.")

            elif dir_path.is_file():

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
                    raise ValueError("You have no tokens remaining. Please upgrade your plan at https://app.prism-ai.ch/ to continue using prism.")
                if file_size > 4 * 1024 * 1024 * 1024:
                    raise ValueError("The file you provided is too large. The maximum file size is 4GB.")
                if str(source).split(".")[-1] not in supported_file_types:
                    raise ValueError("The file you provided is not supported. \nSupported file types are: \n\n - pdf \n - doc \n - docx \n - txt \n - md \n - odt")

                with open(source, 'rb') as file:
                    
                    unique_name = name
                    filename = "kb_"+str(kb_id)+"/"+str(dir_path.name)
                    print("Uploading file "+str(source)+" as "+str(name)+" ...")

                    file_like = FileWithProgress(file, file_size)
                    generate_meta_context = params.pop("generate_meta_context", False)
                    kb_meta_context = params.pop("kb_meta_context", "")

                    headers = instance.create_headers(kb_id=kb_id, unique_name=unique_name, filepath=filename, generate_meta_context=generate_meta_context, kb_meta_context=kb_meta_context)
                    url = instance.api_url + "upload/"

                    with requests.Session() as session: 
                        with tqdm(total=file_size, unit='B', unit_scale=True, dynamic_ncols=True) as progress_bar:
                            response = session.post(url, data=file_like, headers=headers)
                    
                    return response
            else:
                raise ValueError("The path you provided is not valid.")
        else: 
            raise ValueError("The method you provided is not valid. Please use one of the following methods: \n\n - text \n - url \n - file")
