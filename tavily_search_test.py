from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()
import os
TAVILY_API_KEY=os.getenv("sss")
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
response = tavily_client.search("Who is Leo Messi?",max_results=3)

print(response)