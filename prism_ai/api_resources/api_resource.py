from typing import Any
import prism_ai as rs
import requests
import json as jsn
import httpx
from typing import Optional, Any

class APIResource:

    '''
    Parent Class for RenAIssance API Resources 
    '''

    def __init__(
        self,
        endpoint_url: Optional[str],
        response: Optional[requests.Response] = None,
        text: str = "",
        json: dict = {},
        status: int = 0,
    ):

        self.api_key = rs.api_key
        self.api_url = rs.api_url
        self.timeout = rs.timeout
        self.endpoint_url = endpoint_url
        self.response = response
        self.text = text
        self.json = json
        self.status = status

    def __call__(
        self,
        **params: Any,
    ):
        print('This is a parent class for API resource attributes. It is not meant to be called directly. Please refer to our documentation for proper usage of the API.')

    def create_headers(self, kb_id=None, unique_name=None):

        headers = {"Authorization":self.api_key}

        if None not in [kb_id, unique_name]:
            headers['Content-Type'] = 'application/octet-stream'
            headers['Filename'] = unique_name
            headers['Connection'] = 'keep-alive'
            headers['Keep-Alive'] = '300'
            headers['kb_id'] = str(kb_id)
            
        return headers

    def __repr__(self):
        return jsn.dumps(self.json, indent=4, sort_keys=True)

    @classmethod
    def _get(
        cls,
        endpoint_url: Optional[str],
        quiet = False,
        **params,
    ): 

        '''
        Get API Resource
        '''

        if rs.api_key == None: 

            print("Welcome to RenAIssance Studio! To get started, you\'ll need an API Key. \n\n You can get one for free at https://app.renaissancestudio.ai/\n\nOnce you've got your API key, you can either:\n\n- Set it as an environment variable called RS_API_KEY\n- Set it as a variable in your python script called rs.api_key\n\nFor example:\n\nimport renaissance as rs\nrs.api_key = \"YOUR_API_KEY\"\n\nIf you need any help, please refer to our documentation at https://app.renaissancestudio.ai/docs/ \n\nHappy coding!")

            return

        instance = cls(endpoint_url=endpoint_url)
        json, data, params = instance._prepare_params(**params)

        if endpoint_url is None:
            raise ValueError("Endpoint URL is required.")

        else:
            
            if "response_stream" not in endpoint_url:
                # try:
                if True:
                    response = requests.get(
                        instance.api_url + endpoint_url,
                        headers=instance.create_headers(),
                        params=params,
                        data=data,
                        json=json,
                        timeout=instance.timeout,
                    )

                    instance.json = response.json()
                    instance.text = response.text
                    instance.status = response.status_code

                # except:
                else:
                    raise ValueError("There was an error with your request. Please check your parameters and try again.")

                

                for key, value in instance.json.items():
                    setattr(instance, key, value)

        return instance
    

    @classmethod
    def _post(
        cls,
        endpoint_url: Optional[str], 
        **params,
    ):
        '''
        Post API Resource
        '''

        if rs.api_key == None: 

            print("Welcome to RenAIssance Studio! To get started, you\'ll need an API Key. \n\n You can get one for free at https://app.renaissancestudio.ai/\n\nOnce you've got your API key, you can either:\n\n- Set it as an environment variable called RS_API_KEY\n- Set it as a variable in your python script called rs.api_key\n\nFor example:\n\nimport renaissance as rs\nrs.api_key = \"YOUR_API_KEY\"\n\nIf you need any help, please refer to our documentation at https://app.renaissancestudio.ai/docs/ \n\nHappy coding!")

            return


        instance = cls(endpoint_url=endpoint_url)
        json, data, params = instance._prepare_params(**params)

        if instance.endpoint_url is None:
            raise ValueError("Endpoint URL is required.")
        else:
            response = requests.post(
                instance.api_url + instance.endpoint_url,
                headers=instance.create_headers(),
                params=params,
                data=data,
                json=json,
                timeout=instance.timeout,
            )

            print(response.text)

            instance.json = jsn.loads(response.text)
            instance.text = response.text
            instance.status = response.status_code

            for key, value in instance.json.items():
                setattr(instance, key, value)
        
        return instance

    @classmethod
    def _stream(
        cls, 
        endpoint_url: Optional[str],
        quiet: bool = False,
        **params,
    ):
        
        '''
        Get streaming response from API Resource (outputs an object of type generator)
        '''

        if rs.api_key == None: 

            print("Welcome to RenAIssance Studio! To get started, you\'ll need an API Key. \n\n You can get one for free at https://app.renaissancestudio.ai/\n\nOnce you've got your API key, you can either:\n\n- Set it as an environment variable called RS_API_KEY\n- Set it as a variable in your python script called rs.api_key\n\nFor example:\n\nimport renaissance as rs\nrs.api_key = \"YOUR_API_KEY\"\n\nIf you need any help, please refer to our documentation at https://app.renaissancestudio.ai/docs/ \n\nHappy coding!")

            return

        instance = cls(endpoint_url=endpoint_url)
        json, data, params = instance._prepare_params(**params)
        timeout = httpx.Timeout(float(instance.timeout), connect=float(instance.timeout))

        if instance.endpoint_url is None:
            raise ValueError("Endpoint URL is required.")
        
        try:
            
            with httpx.stream(
                method="POST", 
                url=instance.api_url + instance.endpoint_url, 
                headers=instance.create_headers(), 
                timeout = timeout, 
                params=params,
                data=data,
                json=json,
            ) as r:
            
                fulltext = ""
                for chunk in r.iter_text():
                    fulltext += chunk
                    if quiet == False:
                        print(chunk, end="", flush=True)
                    try:
                        yield str(chunk)
                    except KeyError:
                        yield ""
                
        except httpx.RemoteProtocolError as e:

            instance.status = 500
            instance.text = "There\'s been an error on our side. Sorry about that! Our engineers are already contacted and working on a fix. Please try again later."

    @classmethod
    def _no_params_message(
        cls,
        endpoint: str,
        req_pars: list
    ):

        msg = f"You\'ve hit the {endpoint} endpoint, without any parameters.\n\nThe required parameters for this endpoint are:\n- " + "\n- ".join([req_par for req_par in req_pars]) + "\n\nPlease refer to our documentation for a comprehensive list of parameters, and proper usage of the API."
            
        print(msg)
        return None

    @classmethod
    def _prepare_params(
        cls,
        **params,
    ):
        data = {
            
        }

        json = {
            "name": params.pop("name", None),
            "s3_bucket": params.pop("s3_bucket", None),
            "user_prompt": params.pop("user_prompt", None),
            "knowledge_base": "+".join([str(elt) for elt in params.pop("knowledge_base", "")]),
            "url": params.pop("url", None),
            "text": params.pop("text", None),
            "recursion": params.pop("recursion", False),
            "max_recursion": params.pop("max_recursion", 1),
            "only_base_url": params.pop("only_base_url", True),
        }

        params = {
            
        }

        return json, data, params
    
