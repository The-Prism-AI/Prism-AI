from prism_ai.api_resources.api_resource import APIResource
from prism_ai.api_resources.knowledge import Knowledge
import pathlib
import os

supported_file_types = [
    "pdf",
    "doc",
    "docx",
    "txt",
    "md",
    "odt",
    "gz"
]

class KnowledgeBase(APIResource):

    '''
    Knowledge Base Object to be created from a url
    '''


    @classmethod
    def add(
        cls, 
        **params,
    ):
        '''
        Add knowledge to an existing knowledge base
        '''

        kb_id = params.pop("kb_id", None)
        base_dir = params.pop("base_dir", None)
        base_url = params.pop("base_url", None)

        if not ((base_dir is None) ^ (base_url is None)):
            raise ValueError("Please provide either a base directory or a base url, but not both.")

        if None in [kb_id]:
            raise ValueError("Knowledge Base ID not provided.")

        if not base_url is None: 
            if "name" in params:
                return cls._post(
                    endpoint_url=f"users/knowledge_base/{kb_id}/knowledge_from_url/",
                    base_url=base_url,
                    **params,
                )
            else:
                return cls._post(
                    endpoint_url=f"users/knowledge_base/{kb_id}/knowledge_from_url/",
                    # kb_id=kb_id,
                    name = "Knowledge pulled from " + base_url,
                    base_url=base_url,
                    **params,
                )
        
        elif not base_dir is None:

            dir_path = pathlib.Path(base_dir)
            dir_list = list(dir_path.rglob('*'))
            file_list = []
            supported_file_list = []
            to_process = []

            for elt in dir_list:

                if elt.is_dir():
                    print(f"Omitting directory {elt} ... Not a file.")
                    continue
                else:
                    file_list.append(elt)

            print("\n\n")
            for elt in file_list:
                
                if str(elt).split(".")[-1] not in supported_file_types:
                    print(f"Omitting file {elt} ... Unsupported file type.")
                    continue
                else:
                    supported_file_list.append(elt)
            print("\n\n")
            for elt in supported_file_list:
                if os.path.getsize(elt) > 1024 * 1024 * 1024 * 4:
                    print(f"Omitting file {elt} ... File size exceeds 4GB.")
                    continue
                else:
                    to_process.append(elt)

            to_process_size = sum([os.path.getsize(file) for file in to_process])
            info_instance = cls._get(endpoint_url="basic_user_info/", quiet=True)
            user_info = info_instance.json

            if user_info["max_storage"] != None:
                if to_process_size / (1024 * 1024) > user_info["max_storage"]:
                    raise ValueError(f"Attempted to upload {to_process_size / (1024 * 1024)} MB of data, but you have only {user_info['max_storage']} MB of storage available. \n\nPlease upgrade your plan, or attempt upload with fewer data.")
            else: 
                pass
            if user_info["tokens_remaining"] <= 0:
                raise ValueError("You have no tokens remaining. Please upgrade your plan to continue using prism.")
            
            for fl in to_process:
                file = pathlib.Path(fl)
                params.pop("name", None)
                Knowledge.create(
                    method="file",
                    name=file.name,
                    source=file,
                    kb_id=kb_id,
                    **params,
                )
            
            return cls._get(
                endpoint_url=f"users/knowledge_base/{kb_id}/",
                # **params,
            )
        else:
            raise ValueError("Please provide either a base directory or a base url, but not both.")
        
    @classmethod
    def get(
        cls,
        **params,
    ):
            
        '''
        Get a Knowledge Base Object 
        '''

        kb_id = params.pop("kb_id", None)

        if None in [kb_id]:
                
            cls._no_params_message(
                
                endpoint="KnowledgeBase",
                req_pars=[
                    "kb_id",
                ],
            )
            return None
        
        else:

            verbosity = params.pop("verbose", False)
                
            return cls._get(
                endpoint_url=f"users/knowledge_base/{kb_id}/",
                verbose = verbosity,
            )

    @classmethod
    def create(
        cls,
        **params,
    ):
            
        '''
        Create a new Knowledge Base Object 
        '''

        name = params.pop("name", None)

        if None in [name]:
            
            cls._no_params_message(
                
                endpoint="KnowledgeBase",
                req_pars=[
                    "name",
                ],
            )
            return None

        else:

            instance = cls._post(
                endpoint_url=f"users/knowledge_base/",
                name=name,
                **params,
            )
            
            if "base_dir" in params or "base_url" in params:

                instance.add(kb_id=instance.json['id'], name=name, **params)

            return instance

    @classmethod
    def delete(
        cls,
        **params,
    ):
            
        '''
        Delete a Knowledge Base Object 
        '''

        kb_id = params.pop("kb_id", None)

        if None in [kb_id]:
            
            cls._no_params_message(
                
                endpoint="KnowledgeBase",
                req_pars=[
                    "kb_id",
                ],
            )
            return None

        else:

            return cls._delete(
                endpoint_url=f"users/knowledge_base/{kb_id}/",
                **params,
            )
