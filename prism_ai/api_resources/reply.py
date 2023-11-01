from prism_ai.api_resources.api_resource import APIResource

class Reply(APIResource):

    '''
    Reply Object to be created
    '''
    def __init__(self, endpoint_url=None):
        super().__init__(endpoint_url=endpoint_url)

    @classmethod
    def create(
        cls,
        **params,
    ):
            
        '''
        Create a new Reply
        '''

        prompt = params.pop("prompt", None)

        if prompt == None:
            
            cls._no_params_message(
                
                endpoint="reply",
                req_pars=[
                    "prompt"
                ],
            )
            return None
        
        else: 
            return cls._post(
                endpoint_url="response/",
                user_prompt=prompt,
                **params,
            )
        
    @classmethod
    def stream(
        cls,
        **params,
    ):
        
        prompt = params.pop("prompt", None)

        if prompt == None:
            
            cls._no_params_message(
                
                endpoint="reply",
                req_pars=[
                    "prompt"
                ],
            )
            return None
        
        else: 
            a = cls._stream(
                endpoint_url="response_stream/",
                user_prompt=prompt,
                **params,
            )
            for elt in a:
                pass
