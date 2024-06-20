<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT HEADER -->
<br />
<div>

<h1>RAG LLM Chain</h1>

  <p>
    An LLM Chain Python Script utilizing Retrieval Augmented Generation (RAG)
    <br />
    <a href="https://github.com/kgarner-dev/RAG-LLM-Chain/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/kgarner-dev/RAG-LLM-Chain/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

In the summer of 2023, a news story began circulating reporting that a lawyer used ChatGPT to draft his court filings, only to later discover that the language model had referenced fabricated court cases in the draft. This is just one of many examples of the severe repercussions that can arise from the ‘hallucinations’ of these AI models.

Hallucinations are incorrect or misleading information provided by AI language models. These hallucinations can occur for various reasons, one of the most prominent being the inclusion of biases and fictitious information in training data. While these large models are trained on millions of lines of text and content, much of it can include opinionated, falsified, or fictitious material. This can lead to the generation of skewed or false information by these models.

One methodology to combat these hallucinations is the implementation of Retrieval Augmented Generation (RAG). RAG involves the use of an external knowledge base from which the LLM can generate its answers. This approach adds a layer of protection to language models by introducing an authoritative, personalized, and factual knowledge base to pull information and context from.

This Python script creates an LLM chain that employs RAG utilizing OpenAI and Pinecone

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![Python][python]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

1. Get an OpenAI API Key at [https://openai.com/index/openai-api/](https://openai.com/index/openai-api/)
2. After you get your API Key, you will need to pick out a embedding model (text-embedding-ada-002 is used in the code already), along with a GPT Model (gpt-3.5-turbo-16k-0613 is used in the code already)
3. Sign up for a Pinecone account at [https://www.pinecone.io/](https://www.pinecone.io/)
4. Create a Pinecone Index and upload your files with the following information: a unique ID, vector embedding as the value, and the context as the metadata
5. WARNING: When you create vector embeddings to upload to Pinecone, the dimensions of the Index you create need to match the embedding model you select (text-embedding-ada-002 has a dimension of 1536).
<br />

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kgarner-dev/RAG-LLM-Chain.git
   ```
2. Install packages
   ```sh
   pip3 install langchain pinecone-client langchain-openai
   ```

### Instructions

1. Run the Script
   ```sh
   python3 rag_chain.py
   ```
2. Enter Pinecone API
   ```sh
   Enter your Pinecone API Key: 
   ```
3. Enter Pinecone Index
   ```sh
   Enter your Pinecone Index Name:
   ```
4. Enter OpenAI API Key
   ```sh
   Enter your OpenAI API Key:
   ```
4. Enter your Question
   ```sh
   Enter your Question:
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

* Assisting researchers by retrieving relevant academic papers, patents, and technical documents
* Assisting financial analysts by retrieving relevant financial reports, news articles, and market data.
* Assisting writers and content creators by providing background information and references for their topics.
* Providing technical support by retrieving relevant documentation, user manuals, and troubleshooting guides.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

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

Kaleb Garner - [kgarner-dev](https://github.com/kgarner-dev)

Project Link: [https://github.com/kgarner-dev/RAG-LLM-Chain](https://github.com/kgarner-dev/RAG-LLM-Chain)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Lawyer Used ChatGPT In Court—And Cited Fake Cases. A Judge Is Considering Sanctions - Forbes](https://www.forbes.com/sites/mollybohannon/2023/06/08/lawyer-used-chatgpt-in-court-and-cited-fake-cases-a-judge-is-considering-sanctions/)
* [What are AI hallucinations? - Google](https://cloud.google.com/discover/what-are-ai-hallucinations)
* [What is RAG (Retrieval-Augmented Generation)? - Amazon](https://aws.amazon.com/what-is/retrieval-augmented-generation/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kgarner-dev/RAG-LLM-Chain.svg?style=for-the-badge
[contributors-url]: https://github.com/kgarner-dev/RAG-LLM-Chain/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kgarner-dev/RAG-LLM-Chain.svg?style=for-the-badge
[forks-url]: https://github.com/kgarner-dev/RAG-LLM-Chain/network/members
[stars-shield]: https://img.shields.io/github/stars/kgarner-dev/RAG-LLM-Chain.svg?style=for-the-badge
[stars-url]: https://github.com/kgarner-dev/RAG-LLM-Chain/stargazers
[issues-shield]: https://img.shields.io/github/issues/kgarner-dev/RAG-LLM-Chain.svg?style=for-the-badge
[issues-url]: https://github.com/kgarner-dev/RAG-LLM-Chain/issues
[license-shield]: https://img.shields.io/github/license/kgarner-dev/RAG-LLM-Chain.svg?style=for-the-badge
[license-url]: https://github.com/kgarner-dev/RAG-LLM-Chain/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kalebgarner/
[product-screenshot]: images/screenshot.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
