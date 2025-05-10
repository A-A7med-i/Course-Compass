import os

# Application metadata
PROJECT_NAME = "CourseCompass"
VERSION = "1.0.0"
AUTHOR = "Ahmed"
DESCRIPTION = "An AI agent to help find the best courses."


# Model configuration
MODEL_NAME = "groq/llama-3.3-70b-versatile"
TEMPERATURE = 0

# Paths and file locations
AGENT_CONFIG_PATH = "/media/ahmed/Data/CourseCompass/config/agent_param.yaml"
TASK_CONFIG_PATH = "/media/ahmed/Data/CourseCompass/config/task_param.yaml"
LOG_FILE = "logging.log"
LOG_DIR = "/media/ahmed/Data/CourseCompass/logs"


# Logging configuration
LOGGING_FORMAT = (
    "[%(asctime)s] [%(levelname)s] [%(name)s:%(funcName)s:%(lineno)d] - %(message)s"
)
DATEFMT = "%Y-%m-%d %H:%M:%S"


# API keys and credentials
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SCRAPING_API_KEY = os.getenv("SCRAPING_API_KEY")

# Schemas constant
NO_KEYWORDS = 10


# Crew inputs
INPUTS = {
    "course_name": "Python Programming",
    "websites_list": [
        "Coursera",
        "Udemy",
        "edX",
        "Pluralsight",
        "LinkedIn Learning",
    ],
    "country_name": "United States",
    "language": "English",
    "no_keywords": NO_KEYWORDS,
    "score_th": 0.7,
    "top_recommendations_no": 5,
    "company_name": "TechCorp Inc.",
}

# OUTS files
SEARCH_QUERIES_OUT = "/media/ahmed/Data/CourseCompass/outs/search_queries_agent.json"
SEARCH_ENGINE_OUT = "/media/ahmed/Data/CourseCompass/outs/search_engine_agent.json"
SCRAPING_OUT = "/media/ahmed/Data/CourseCompass/outs/scraping_agent.json"
REPORTER_OUT = "/media/ahmed/Data/CourseCompass/outs/reporter_agent.html"
