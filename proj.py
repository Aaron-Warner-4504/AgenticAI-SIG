from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
load_dotenv()  # Load environment variables from .env file
import datetime
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_classic import hub
from langchain_core.prompts import ChatPromptTemplate

llm=ChatGroq(model="llama-3.3-70b-versatile")

@tool
def get_system_time(format:str="%Y-%m-%d %H:%M:%S"):
    """Get the current system time in the specified format."""
    
    curr_time=datetime.datetime.now()
    formatted_time=curr_time.strftime(format)
    return formatted_time

prompt_template=hub.pull("hwchase17/react")

query="What is the current time in the format YYYY-MM-DD HH:MM:SS?"

tools=[get_system_time]

agent=create_agent(llm,tools,prompt_template)




result=agent.invoke({"input":query})
print(result['output'])  # Print the output of the agent's response