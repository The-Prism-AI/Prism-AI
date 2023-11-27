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
        prompt: str,
        **params,
    ):
            
        '''
        Create a new Reply
        '''

        return cls._post(
                endpoint_url="response/",
                user_prompt=prompt,
                **params,
            )
        
    @classmethod
    def stream(
        cls,
        prompt: str,
        **params,
    ):

        return cls._stream(
                endpoint_url="response_stream/",
                user_prompt=prompt,
                **params,
            )
