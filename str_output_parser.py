from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = ChatGoogleGenerativeAI(model = 'gemini-3.8-flash')
parsers = StrOutputParser()
template1 =  PromptTemplate(template='write me a detail note on {topic}',input_variables=['topic'])
template2 =  PromptTemplate(template='give me 5 points on this {text}',input_variables=['text'])

chain = template1|llm|parsers|template2|llm|parsers
output =chain.invoke({'topic':'black hole'})
print(output)

