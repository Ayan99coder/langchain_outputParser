# LangChain Output Parser Playground

A clean, practical example repository for learning and experimenting with LangChain output parsing techniques using String, JSON, and Pydantic output parsers.

<p align="center">
  <img src="https://img.shields.io/badge/LangChain-Output%20Parser-0A0A0A?style=for-the-badge&logo=python&logoColor=white" alt="LangChain Output Parser" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/LLM-Integration-4B5563?style=for-the-badge" alt="LLM Integration" />
</p>

## Overview

This project demonstrates how to structure LangChain chains that convert model responses into clean, machine-readable outputs.

It includes examples for:

- String output parsing with `StrOutputParser`
- JSON output parsing with `JsonOutputParser`
- Structured output parsing with `PydanticOutputParser`

This repository is ideal for developers who want to understand how to enforce schema-based outputs from LLMs in real-world applications.

## Why this matters

LLMs often return free-form text, which is difficult to work with in production systems. Output parsers help convert raw model output into:

- plain strings
- valid JSON
- validated Pydantic models

This makes the results easier to use in downstream application logic, APIs, dashboards, and databases.

## Project Structure

```text
langchain_outputParser/
├── str_output_parser.py
├── json_output_parser.py
├── pydantic_output_parser.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt   # optional if added later
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ayan99coder/langchain_outputParser.git
cd langchain_outputParser
```

2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install langchain langchain-core langchain-google-genai langchain-huggingface python-dotenv pydantic
```

## Environment Setup

This project may use Google Generative AI and environment variables.

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

If you are using Hugging Face models, make sure your environment is configured accordingly and that the selected model is available.

## Examples

### 1) String Output Parser

The file `str_output_parser.py` demonstrates a chain that generates text and transforms it through `StrOutputParser`.

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(model='gemini-3.8-flash')
parser = StrOutputParser()

template = PromptTemplate(
    template='write me a detailed note on {topic}',
    input_variables=['topic']
)

chain = template | llm | parser
output = chain.invoke({'topic': 'black hole'})
print(output)
```

### 2) JSON Output Parser

The file `json_output_parser.py` shows how to request output in a structured JSON format.

```python
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

chain = (
    PromptTemplate(
        template='give me name, age, college and about his mentality of 5 fictional persons {typeOfData}',
        input_variables=[],
        partial_variables={'typeOfData': parser.get_format_instructions()}
    )
    | model
    | parser
)

result = chain.invoke({})
print(result)
```

### 3) Pydantic Output Parser

The file `pydantic_output_parser.py` uses a `BaseModel` schema to enforce a structured response.

```python
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Person(BaseModel):
    name: str = Field(description='Name of person')
    age: str = Field(description='Age of person')
    city: str = Field(description='City of person')

parser = PydanticOutputParser(pydantic_object=Person)
```

This ensures the model output stays aligned with the defined schema instead of producing unstructured text.

## Use Cases

- Extracting structured data from LLM responses
- Building AI-powered forms and data pipelines
- Creating JSON APIs from model results
- Validating generated content before storing or displaying it
- Building research assistants and workflow automation

## Notes

- Make sure your API keys and credentials are stored securely.
- Use `.env` files for local development.
- For production, prefer robust validation and guardrails around LLM outputs.
- Output parsers help reduce hallucinated or malformed responses, but they do not replace application-level validation.

## License

This project is open for experimentation and learning purposes.

## Connect

If you are building with LangChain and structured outputs, this repository is a good foundation to extend into more advanced agent workflows, database integrations, and API-based applications.

---

Built for learning, experimentation, and production-ready structured LLM output design.
