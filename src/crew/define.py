from src.tools.tool import search_tool, scraping_tool
from src.agents.agent import AgentFactory
from src.tasks.task import TaskManager
from src.constants.constant import *
from src.schemas.schema import *

agents = AgentFactory()

tasks = TaskManager()

search_query_agent = agents.create_agent("search_queries_agent")

search_engine_agent = agents.create_agent("search_engine_agent", tools=[search_tool])

scraping_agent = agents.create_agent("scraping_agent", tools=[scraping_tool])

reporter_agent = agents.create_agent("reporter_agent")

search_queries_task = tasks.create_task(
    "search_queries_task",
    output_json=SearchQueries,
    output_file=SEARCH_QUERIES_OUT,
    agent=search_query_agent,
)


search_engine_task = tasks.create_task(
    "search_engine_task",
    output_json=AllSearchResults,
    output_file=SEARCH_ENGINE_OUT,
    agent=search_engine_agent,
)


scraping_task = tasks.create_task(
    "scraping_task",
    output_json=ScrapingResult,
    output_file=SCRAPING_OUT,
    agent=scraping_agent,
)


reporter_task = tasks.create_task(
    "reporter_task", output_file=REPORTER_OUT, agent=reporter_agent
)
