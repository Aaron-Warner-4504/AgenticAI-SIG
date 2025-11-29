from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv() 

llm=ChatGroq(model="llama-3.3-70b-versatile")

messages=[
    SystemMessage(content="You are a helpful assistant "),
    HumanMessage(content="Write a poem about AI in 4 lines")
]

result=llm.invoke(messages)
print(result.content)