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
  <a href="https://github.com/Renaissance-Studio/Prism-AI">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/Renaissance-Studio/Prism-AI"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Renaissance-Studio/Prism-AI">View Demo</a>
    ·
    <a href="https://github.com/Renaissance-Studio/Prism-AI/issues">Report Bug</a>
    ·
    <a href="https://github.com/Renaissance-Studio/Prism-AI/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You'll need python version 3.7 or higher to use the Prism AI API wrapper.

### Installation

1. Get a free API Key at [https://www.prism-ai.ch/](https://www.prism-ai.ch/)
2. Install Prism-AI package 
   ```sh
   pip install prism_ai
   ```
4. Enter your API as an environment variable, OR specify within python itself
   ```sh
   export PRISM_API_KEY="rs_123...456"
   ```
   OR
   ```py
   import prism_ai as pai
   pai.api_key = "rs_123...456"
   ```
5. Start Building! 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Knowledge

A "Knowledge" object is a bunch of text which you can let your AI model reference. You can feed text data to a knowledge object either via: 

 1. Specifying a URL that Prism will crawl for text data, (i.e.):

    ```py
    knowledge = pai.Knowledge.create(
      method = "url", # The knowledge extraction method
      name = "prism knowledge", # A name for your knowledge object 
      kb_id = 1, # The knowledge base id which this knowledge should belong to 
      url = "https://www.prism-ai.ch/", # The url to scrape (NOTE: only https will work. http urls will be rejected.)
    )
    ```

  Similarly, you can crawl a url recursively to extract and crawl all links, sublinks, and sub-sublinks etc... found on a webpage, up to the maximum recursion level (automatically capped at 100)

    ```py
    knowledge = pai.Knowledge.create(
        method = "url",
        name = "prism knowledge",
        kb_id = 1,
        url = "https://www.prism-ai.ch/",
        recursion = True, # Set to False by default
        max_recursion = 50, # Number of linked pages to also scrape
        only_base_url = False # Specifies whether or not to accept linked urls outside the provided domain network location
      )
    ```

 2. Specifying a Path to a file or directory where Prism will extract text data, 

    ```py
      knowledge = pai.Knowledge.create(
        method = "path",
        name = "prism knowledge",
        kb_id = 1,
        text = "/home/prism_user/Desktop/useful_knowledge.pdf" 
      )
    ```

 3. Specifying a string to be added directly to the knowledge

    ```py
      knowledge = pai.Knowledge.create(
        method = "text",
        name = "prism knowledge",
        kb_id = 1,
        url = "Peter Piper picked a peck of pickled peppers." 
      )
    ```
    
 4. Plug in directly to your Google Drive, One Drive, Sharepoint, Nextcloud, ... (Coming Soon!)

Note that specifying knowledge via Raw Text is the most customizable method by which to add knowledge to a Knowledge Base, however requires the most customization from the client. Alternatively, you can use our built in web-scrapers (point 2 above) to scrape text data from hundreds of websites siumltaneously and immediately use the resulting data in your R.A.G. pipeline. 

### Knowledge Bases 

Knowledge bases provide the organizational structure of your textual information. You can create a knowledge base like this: 

```
pai.KnowledgeBase.create(
  name="The name of your KnowledgeBase"
)
```

You can additionally add knowledges directly to a knowledge base by specifying them within the knowledge creation call: 

```py
kb = pai.KnowledgeBase.create(
        knowledges = ["https://www.narwhal.ch/about", "https://www.gwcustom.com/about/"],
        names = ["test1", "test2"],
        name = "Test knowledge base"
        )

```

### Reply

Prism will directly forward your context to OpenAI (or your LLM provider of choice) using the Reply function: 

```py
reply = pai.Reply.create(
  prompt = "Tell me something Interesting that about prism-ai.",
  knowledge_base = []
)
```

Having been provided the relevant information from our homepage, the model is able to successfully answer questions about prism! 

You can also stream your response: 

```py
reply = pai.Reply.stream(
  prompt = "What is the only pair of twin primes whose difference is just 1?",
  knowledge_bases = [2,3]
)
```

_For more examples, please refer to the [Documentation](https://www.prism-ai.ch/)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/Renaissance-Studio/Prism-AI/issues) for a full list of proposed features (and known issues).

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

Project Link: [https://github.com/Renaissance-Studio/Prism-AI](https://github.com/Renaissance-Studio/Prism-AI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/Renaissance-Studio/Prism-AI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Renaissance-Studio/Prism-AI.svg?style=for-the-badge
[forks-url]: https://github.com/Renaissance-Studio/Prism-AI/network/members
[stars-shield]: https://img.shields.io/github/stars/Renaissance-Studio/Prism-AI.svg?style=for-the-badge
[stars-url]: https://github.com/Renaissance-Studio/Prism-AI/stargazers
[issues-shield]: https://img.shields.io/github/issues/Renaissance-Studio/Prism-AI.svg?style=for-the-badge
[issues-url]: https://github.com/Renaissance-Studio/Prism-AI/issues
[license-shield]: https://img.shields.io/github/license/Renaissance-Studio/Prism-AI.svg?style=for-the-badge
[license-url]: https://github.com/Renaissance-Studio/Prism-AI/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
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
