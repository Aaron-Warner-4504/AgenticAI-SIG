from dotenv import load_dotenv
load_dotenv()
from tavily import TavilyClient
import datetime
import os
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage,SystemMessage
from langchain_classic import hub
from langchain.agents import create_agent
import requests
TAVILY_API_KEY=os.getenv("sss")
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
OPENWAEATHER_API_KEY=os.getenv("OPENWEATHER_API_KEY")

# @tool

# def get_weather(city: str, api_key: str = OPENWAEATHER_API_KEY) -> dict:
#     """
#     Returns current weather info for a given city.
#     """

#     if api_key is None:
#         return {"error": "Missing OPENWEATHER_API_KEY in environment"}

#     url = (
#         f"https://api.openweathermap.org/data/2.5/weather?q={city}"
#         f"&appid={api_key}&units=metric"
#     )

#     response = requests.get(url)

#     if response.status_code != 200:
#         return {
#             "error": f"API error: {response.status_code}",
#             "details": response.text
#         }

#     data = response.json()

#     return {
#         "city": data["name"],
#         "temperature": data["main"]["temp"],
#         "feels_like": data["main"]["feels_like"],
#         "humidity": data["main"]["humidity"],
#         "weather": data["weather"][0]["description"],
#         "wind_speed": data["wind"]["speed"]
#     }
# # Example Usage:
# # print(get_weather("Pune", "YOUR_API_KEY"))




@tool
def tavily_search_tool(query: str, max_results: int = 5) -> dict:
    """This tool performs web search using Tavily web search API and this gives output in json format."""

    response = tavily_client.search(query=query, max_results=max_results)
    return response





@tool
def get_system_time(format:str="%Y-%m-%d %H:%M:%S"):
    """Get the current system time in the specified format."""
    
    curr_time=datetime.datetime.now()
    formatted_time=curr_time.strftime(format)
    return formatted_time


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    
)

# Pull ReAct prompt from the hub
react_prompt = hub.pull("hwchase17/react")


system_prompt_text = react_prompt.template


agent = create_agent(
    model=llm,
    tools=[get_system_time, tavily_search_tool],
    system_prompt=system_prompt_text,
)


query = "Do a web search and tell me who won IPL 2025 final?Also, give me today's date"

result = agent.invoke({"messages": [HumanMessage(content=query)]})
# print(result)
ai_messages = [msg for msg in result["messages"] if isinstance(msg, AIMessage)]

for i,msg in enumerate(ai_messages,1):
    print(f"AI Message {i}:\n{msg.content}\n")


if ai_messages:
    print("Final AI Message:\n", ai_messages[-1].content)

