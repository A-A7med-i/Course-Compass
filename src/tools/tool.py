from src.schemas.schema import Recommendation
from src.constants.constant import *
from scrapegraph_py import Client
from tavily import TavilyClient
from crewai.tools import tool


@tool
def search_tool(query: str):
    """
    Search the web for information based on the provided query.

    Args:
        query: The search query string

    Returns:
        Search results from Tavily
    """
    search_client = TavilyClient(api_key=TAVILY_API_KEY)
    return search_client.search(query)


@tool
def scraping_tool(page_url: str):
    """
    Scrape a webpage and extract structured information according to the Recommendation schema.

    Args:
        page_url: The URL of the webpage to scrape

    Returns:
        A dictionary containing the page URL and extracted details
    """
    scraping_client = Client(api_key=SCRAPING_API_KEY)
    details = scraping_client.smartscraper(
        page_url=page_url,
        user_prompt="Extract '''json\n"
        + Recommendation.model_json_schema()
        + "'''\n From the web page",
    )
    return {"page_url": page_url, "details": details}
