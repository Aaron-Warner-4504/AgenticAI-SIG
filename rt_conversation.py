from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
load_dotenv()

llm=ChatGroq(model="llama-3.3-70b-versatile")

sys_message=SystemMessage(content="You are a helpful assistant ")

chat_history=[]

while(True):
    query=input("User: ")
    if(query.lower()=="exit"):
        break

    chat_history.append(HumanMessage(content=query))

    result=llm.invoke(chat_history)

    print("AI Response: "+ result.content)

    chat_history.append(AIMessage(content=result.content))

print("\n ----------------Message History-------------")
print(chat_history)