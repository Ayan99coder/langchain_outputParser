from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
llm = HuggingFacePipeline.from_model_id(
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
  task="text-generation",
  )
model = ChatHuggingFace(llm = llm)
class Person(BaseModel):
    name : str = Field(
    description='Name of person'
    ),
    age : str = Field(
    description='age of person'
        ),
    city : str = Field(
    description='city of person'
        )
parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate( template=""" Generate the name, age and city of one fictional Pakistani person. {text} {format} Return ONLY the JSON object. Do not return the schema. Do not include explanations. """, input_variables=["text"], partial_variables={ "format": parser.get_format_instructions() } )
chain = template|model|parser
output = chain.invoke({'text': 'pakistani'})
print(output)
