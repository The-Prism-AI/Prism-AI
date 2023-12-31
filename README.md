<!-- Improved compatibility of back to top link -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/The-Prism-AI/Prism-AI">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Prism AI</h3>

  <p align="center">
    Prism AI empowers developers to easily implement A.I.-powered search and retrieval augmented generation, in just a few lines of code. 
    <br />
    <a href="https://www.prism-ai.ch/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/The-Prism-AI/Prism-AI/issues">Report Bug</a>
    ·
    <a href="https://github.com/The-Prism-AI/Prism-AI/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://app.prism-ai.ch/)

**Prism** is an innovative platform designed to simplify the integration of Retrieval Augmented Generation (RAG) capabilities into your applications. RAG combines the power of large language models with the ability to retrieve and incorporate information from knowledge sources seamlessly. It enhances the text generated by AI models, such as ChatGPT, Bard or Claude, by incorporating real-world knowledge.

**RAG** is a groundbreaking approach in the field of AI that allows developers to tap into the vast knowledge available in databases, websites, and files. By integrating this knowledge, developers can create AI systems that provide accurate and contextually relevant information. RAG is particularly valuable in tasks such as document search, question-answering, and chatbots, where understanding context and retrieving relevant information are crucial.

**Vector embeddings**, a key component of RAG systems, play a crucial role in capturing the semantic meaning of words and phrases. These embeddings transform text into high-dimensional numerical representations, enabling AI models to compare and identify similar information effectively. Vector embeddings have been instrumental in advancing RAG systems by providing a nuanced understanding of information and improving search capabilities.

**Vector Embeddings are not Enough!** Prism takes RAG to the next level by offering powerful **Multidimensional Index Structures**, **Named Entity Recognition** and subsequent **Knowledge-Graph Retrieval**, and more. Through Prism's intuitive API and libraries available in multiple languages, including Python and JavaScript, developers can quickly integrate RAG capabilities into their applications. Whether you are an expert or just getting started with language models, Prism's user-friendly platform simplifies the process of incorporating real-world knowledge into your AI applications.
  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You'll need python version 3.7 or higher to use the Prism AI API wrapper.

## Installation and Setup

Prism is ready to go out of the box. The only major steps for setup are: 

### Install Prism with pip 

```sh
pip install prism_ai
```
### Get an API Key 

You can generate an API key by creating an account [here](https://www.prism-ai.ch/) and adding an API key directly in the application. Make sure to store it somewhere, you'll never see it again after it's created. 

### Add your API key as an environment variable 

```sh 
export PRISM_API_KEY=rs_123...def
```

Or to set your API key directly in python you can run: 

```py
import prism_ai as pai
pai.api_key = "rs_123...def"
```

## Quick Start

After installing prism, you can start adding knowledge bases, and generating replys based on the information contained within them: 

```py

kb1 = pai.KnowledgeBase.create(
  name = "Online Information", 
  base_url = "https://www.my-website.com/",
)

kb2 = pai.KnowledgeBase.create(
  name = "Local Information", 
  base_dir = "/path/to/relevant/directory"
)

reply = pai.Reply.stream(
  prompt="Tell me about some of the information contained in the website and files.",
  kb_ids=[kb1.id, kb2.id]
)

```


## Standalone Methods 

### Info

```py
pai.info()
```

#### Summary 

Assuming the API key has been specified and you have a stable connection to the internet, the info function will return a breakdown of the user info, as well as the knowledge-graph tree containing a list of all knowledge bases, and a list of all contained knowledges for each knowledge base. 

This function has no required or optional parameters.

## Resource Methods

### Knowledge Bases

#### Create a Knowledge Base

**Summary:**

Knowledge bases provide the organizational structure of your textual information. Knowledge Bases contain individual Knowledges. This function is used to create a knowledge base. 

**Required Parameters:**

*__name__: str* - This is the name you will assign to your knowledge base.  

**Optional Parameters:**

*__base_dir__: str (default: None)* - A path to a directory, where Prism should read files from. Every file from this directory will be processed as individual knowledges, to be added to the new knowledge base.

*__base_url__: str (default: None)* - A url from which Prism should extract relevant context. Only one of base_dir or base_url can be supplied. If both are supplied to the create function, an error will be thrown. 

*__recursion__: bool (default: False)* - Specifies whether knowledge should be added recursively 

*__max_recursion__: int (default: None)* - Specifies the maximum number of files to read from a directory, or urls to scrape from links in the provided base_url.

*__only_base_url__: bool (default: True)* - Specifies whether or not to scrape urls from links which point to network locations, other than the one supplied. For example, if only_base_url is set to True, and base_url is set to "https://www.prism-ai.ch/about/", then Prism will only create context from the urls it finds which also point to a network location belonging to prism-ai.ch. This argument will be ignored if used in combination with the base_dir argument. 

*__kb_meta_context__: str (default: None)* - This string will be supplied to prompts with the context retrieved from this Knowledge Base, any time context is retrieved from this Knowledge Base. Adding relevant meta context, in general, significantly improves an LLM's ability to utilize context and synthesize information which is provided to it. 

*__smart_index__: bool (default: False)* - Specify whether or not to apply Prism's "Smart Index" to the resulting context data. In general, you should keep this option set to False unless you anticipate adding a large amount of information to this knowledge base. You can read more about Prism's Smart Index [here](https://www.prism-ai.ch/).

*__ner__: bool (default: False)* - Specify whether or not to extract named entities from provided text for use in Prism's knowledge graph retrieval engine. 

**Example Usage:**

Create a Knowledge Base from information found on the internet: 

```py
kb = pai.KnowledgeBase.create(
  name = "Online Prism Information", 
  base_url = "https://www.prism-ai.ch/",
  only_base_url = True, 
  recursion = True, 
  max_recursion = 100, 
  kb_meta_context = "This is information which was extracted from Prism's website",
  generate_meta_context = True,
  smart_index = False, 
  ner = True 
)
```

Create a Knowledge Base from information found on a local filesystem: 

```py
kb = pai.KnowledgeBase.create(
  name = "Local Prism Information", 
  base_dir = "/path/to/relevant/directory",
  recursion = True, 
  kb_meta_context = "This is information which was extracted from local files belonging to Prism's team.",
  generate_meta_context = True,
  smart_index = False, 
  ner = True
)
```

**Important Note:** embedding, entity extraction, graph generation, and context organization takes some time, and happens asynchronously with your calls to the API. This means that you will recieve a response from create or add calls to both Knowledge and Knowledge Base objects before they are ready and available to be used for RAG. You can see the availability of your knowledge object at any time by running: 

```py
print(pai.Knowledge.get(knowledge_id=int(your_knowledge_id)))
```

Or alternatively you can retrieve the status of all your knowledge objects by running: 

```py
pai.info()
```

#### Add to an existing Knowledge Base

**Summary:**

Knowledge bases provide the organizational structure of your textual information. Knowledge Bases contain individual Knowledges. This function is used to add to an existing knowledge base. 

**Required Parameters:**

*__kb_id__: int* - This is the ID of the knowledge base you wish to add knowledge to.

**Optional Parameters:**

*__base_dir__: str (default: None)* - A path to a directory, where Prism should read files from. Every file from this directory will be processed as individual knowledges, to be added to the new knowledge base.

*__base_url__: str (default: None)* - A url from which Prism should extract relevant context. Only one of base_dir or base_url can be supplied. If both are supplied to the create function, an error will be thrown. 

*__recursion__: bool (default: False)* - Specifies whether knowledge should be added recursively 

*__max_recursion__: int (default: None)* - Specifies the maximum number of files to read from a directory, or urls to scrape from links in the provided base_url.

*__only_base_url__: bool (default: True)* - Specifies whether or not to scrape urls from links which point to network locations, other than the one supplied. For example, if only_base_url is set to True, and base_url is set to "https://www.prism-ai.ch/about/", then Prism will only create context from the urls it finds which also point to a network location belonging to prism-ai.ch. This argument will be ignored if used in combination with the base_dir argument. 

*__kb_meta_context__: str (default: None)* - This string will be supplied to prompts with the context retrieved from this Knowledge Base, any time context is retrieved from this Knowledge Base. Adding relevant meta context, in general, significantly improves an LLM's ability to utilize context and synthesize information which is provided to it. 

*__generate_meta_context__: bool (default: True)* - This setting determines whether or not to dynamically generate meta-context for each knowledge which is supplied to the knowledge base. Providing both kb_meta_context, and turning on generate_meta_context has been shown to significantly improve retrieval metrics, and subsequent generations.

*__smart_index__: bool (default: False)* - Specify whether or not to apply Prism's "Smart Index" to the resulting context data. In general, you should keep this option set to False unless you anticipate adding a large amount of information to this knowledge base. You can read more about Prism's Smart Index [here](https://www.prism-ai.ch/).

*__ner__: bool (default: False)* - Specify whether or not to extract named entities from provided text for use in Prism's knowledge graph retrieval engine. 

**Example Usage:**

Add information from the internet to an existing knowledge base:

```py
kb = pai.KnowledgeBase.add(
  kb_id = 1, 
  base_url = "https://www.prism-ai.ch/",
  only_base_url = True, 
  recursion = True, 
  max_recursion = 100, 
  kb_meta_context = "This is information which was extracted from Prism's website",
  generate_meta_context = True,
  smart_index = False, 
  ner = True 
)
```

**Important Note:** embedding, entity extraction, graph generation, and context organization takes some time, and happens asynchronously with your calls to the API. This means that you will recieve a response from create or add calls to both Knowledge and Knowledge Base objects before they are ready and available to be used for RAG. You can see the availability of your knowledge object at any time by running: 

```py
print(pai.Knowledge.get(knowledge_id=int(your_knowledge_id)))
```

Or alternatively you can retrieve the status of all your knowledge objects by running: 

```py
pai.info()
```

#### Get Details on a Specific Knowledge Base 

**Summary:**

Here we provide a function for retrieve details about a specific knowledge base. 

**Required Parameters:**

*__kb_id__: int* - This is the ID of the knowledge base you wish to add knowledge to.

**Optional Parameters:**

*__verbose__: bool (default: False)* - Specify whether or not to include details about all knowledge objects contained within the specified knowledge base.

**Example Usage:**

Get details about a knowledge base, by knowledge base id, from Prism

```py
pai.KnowledgeBase.get(
  kb_id = 1, 
  verbose = False
)
```

#### Delete a Knowledge Base

**Summary:**

This function is used to delete a knowledge base. This action is irreversable and should be used with caution. 

**Required Parameters:**

*__kb_id__: int* - This is the ID of the knowledge base you wish to delete.

**Optional Parameters:**

None

**Example Usage:**

```py
kb = pai.KnowledgeBase.delete(
  kb_id = 1
)
```

### Knowledge 

#### Create Knowledge

**Summary:**

Knowledges contain context for a LLM to use for improving generations. Every knowledge is contained within a single knowledge base. Knowledges can be created from a webpage, a file, a user-supplied string of text, or an audio / video file (coming soon). 

**Required Parameters:**

*__method__: str* - Can be one of: "url", "text" or "file", indicating whether to grab knowledge from a url, from a user-supplied string, or a file, respectively. Supported filetypes are pdf, doc, docx, txt, odt and md. URLs must be prefixed with https or they will not be indexed. 

*__name__: str* - The name you wish to give your knowledge. 

*__kb_id__: int* - The ID of the knowledge base where you wish to create this knowledge. 

*__source__: str* - The url, filesystem path, or user-supplied string which you wish to add to the knowledge base.

**Optional Parameters:**

*__meta_context__: str (default: None)* - This string will be supplied to prompts with the context retrieved from this Knowledge, any time context is retrieved from this Knowledge, in addition to the meta context attached to the parent knowledge base. Adding relevant meta context, in general, significantly improves an LLM's ability to utilize context and synthesize information which is provided to it. If meta_context is not supplied, meta_context will be automatically generated for the knowledge object in the background. 

**Example Usage:**

Creating a knowledge from a url: 

```py
knowledge = pai.Knowledge.create(
  method = "url", 
  name = "Knowledge about Prism", 
  kb_id = 1, 
  source = "https://www.prism-ai.ch/",
  meta_context = "This is information retrieved from the Prism website."
)
```

Creating a knowledge from a file: 

```py
knowledge = pai.Knowledge.create(
  method = "file", 
  name = "Knowledge about Prism", 
  kb_id = 1, 
  source = "/path/to/prism.pdf",
  meta_context = "This is information retrieved from the Prism documentation."
)
```

Creating a knowledge from a file: 

```py
knowledge = pai.Knowledge.create(
  method = "text", 
  name = "Knowledge about Prism", 
  kb_id = 1, 
  source = "Did you know that Prism supports fully private instances? That means nobody but you ever touches your data!",
  meta_context = "This is information retrieved from the Prism documentation."
)
```

**Important Note:** embedding, entity extraction, graph generation, and context organization takes some time, and happens asynchronously with your calls to the API. This means that you will recieve a response from create or add calls to both Knowledge and Knowledge Base objects before they are ready and available to be used for RAG. You can see the availability of your knowledge object at any time by running: 

```py
print(pai.Knowledge.get(knowledge_id=int(your_knowledge_id)))
```

Or alternatively you can retrieve the status of all your knowledge objects by running: 

```py
pai.info()
```

#### Delete 

**Summary:**

This function is used to delete a knowledge. This action is irreversable and should be used with caution. 

**Required Parameters:**

*__knowledge_id__: int* - This is the ID of the knowledge you wish to delete.

**Optional Parameters:**

None

**Example Usage:**

```py
to_delete = pai.Knowledge.delete(
  knowledge_id = 1
)
```

### Reply

**Summary:**

This endpoint allows you to forward context directly to the LLM of your choice. Using Reply objects is more powerful, and usually faster, than retrieving context and sending to an LLM yourself. This is due in part to the various prompt schemas we have tested and created meticulously to maximize performance in the backend, as well as the remaining part of our RAG pipeline which get's dropped when retrieving context directly to your own internal application. 

#### Create a Reply

**Summary:**

This endpoint allows you to generate a reply from the LLM of your choice. 

**Required Parameters:**

*__prompt__: str* - This provides a prompt for the LLM from which to generate a reply. 

**Optional Parameters:**

*__kb_id__: List[int] (default: [])* - A list of knowledge base ids from which to retrieve relevant context. 

*__model__: str (coming soon)* - An LLM to use for generating a reply. In the very near future, we aim to offer every model available from OpenAI, Anthropic, Minstral, Google, Meta, and more.  

*__hyde__: bool (default: False)* - Here you can indicate whether you would like to run the HyDE algorithm for RAG. This option is good for short prompts contianing little context to search for. 

**Example Usage:**

Create a reply using some knowledge base: 

```py
reply = pai.Reply.create(
  prompt = "Tell me something Interesting that about prism-ai.",
  knowledge_base = [1],
  hyde = True
)
```

#### Create a Reply Stream 

**Summary:**

This endpoint allows you to generate a reply stream from the LLM of your choice. 

**Required Parameters:**

*__prompt__: str* - This provides a prompt for the LLM from which to generate a reply. 

**Optional Parameters:**

*__kb_id__: List[int] (default: [])* - A list of knowledge base ids from which to retrieve relevant context. 

*__model__: str (coming soon)* - An LLM to use for generating a reply. In the very near future, we aim to offer every model available from OpenAI, Anthropic, Minstral, Google, Meta, and more.  

*__hyde__: bool (default: False)* - Here you can indicate whether you would like to run the HyDE algorithm for RAG. This option is good for short prompts contianing little context to search for. 

**Example Usage:**

Create a reply using some knowledge base: 

```py

stream = pai.Reply.stream(
  prompt = "Tell me something Interesting that about prism-ai.",
  kb_ids = [1],
  hyde = True
)

for chunk in stream:
  # handle the chunk
  pass

```

### Context 

#### get

**Summary:**

Contexts are strings of raw text which has ben harvested from a document, url, or other source of textual information. Contexts belong to knowledge objects. The context endpoint provides an interface for interacting with the context you've created, and performing RAG manually. 

**Required Parameters:**

*__kb_id__: List[int]* - Specify a list of knowledge base ids from which to extract contexts.

*__prompt__: str* - The text to use for context search.

**Optional Parameters:**

*__n__: int (default: 1)* - Specify the number of contexts to retrieve from the knowledge base. 

*__hyde__: bool (default: False)* - Specify whether or not to use the hyde algorithm for context retrieval.

**Example Usage:**

Extract context from your knowledge base:

```py

context = pai.Context.get(
  kb_id = [1, 2, 3],
  prompt = "Here is a prompt that we'll use to search over the knowledge bases specified",
  n = 10, 
  hyde = True
)

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Prism AI - info@prism-ai.ch
<!-- [@twitter_handle](https://twitter.com/twitter_handle)-->

Project Link: [https://github.com/The-Prism-AI/Prism-AI](https://github.com/The-Prism-AI/Prism-AI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/The-Prism-AI/Prism-AI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/The-Prism-AI/Prism-AI.svg?style=for-the-badge
[forks-url]: https://github.com/The-Prism-AI/Prism-AI/network/members
[stars-shield]: https://img.shields.io/github/stars/The-Prism-AI/Prism-AI.svg?style=for-the-badge
[stars-url]: https://github.com/The-Prism-AI/Prism-AI/stargazers
[issues-shield]: https://img.shields.io/github/issues/The-Prism-AI/Prism-AI.svg?style=for-the-badge
[issues-url]: https://github.com/The-Prism-AI/Prism-AI/issues
[license-shield]: https://img.shields.io/github/license/The-Prism-AI/Prism-AI.svg?style=for-the-badge
[license-url]: https://github.com/The-Prism-AI/Prism-AI/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/prism-rag/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
