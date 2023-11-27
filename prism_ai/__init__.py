"""
prism
~~~~~~

The prism python package - a python wrapper for the prism API.
"""

import os

api_key = os.getenv('PRISM_API_KEY')
api_url = "https://api.prism-ai.ch/"
timeout = 30

from prism_ai.api_resources.knowledge import Knowledge
from prism_ai.api_resources.reply import Reply
from prism_ai.api_resources.knowledge_base import KnowledgeBase
from prism_ai.api_resources.api_resource import APIResource


def info(): 

    return APIResource._get(endpoint_url="basic_user_info/")

def __version__():

    """
    Returns information about the current version of the prism package.
    """

    return "0.1.0"