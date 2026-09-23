from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
llm = HuggingFacePipeline.from_model_id(
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
  task="text-generation",
  )
model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()
template = PromptTemplate(template='give me name ,age ,college and about his mentality  of 5 fictional persons {typeOfData}',input_variables=[],partial_variables={'typeOfData':parser.get_format_instructions()})
chain = template | model | parser
result = chain.invoke({})
print(result)