from dataclasses import dataclass
from typing import List


@dataclass
class ProjectStructure:
    directories: List[str] = None
    files: List[str] = None

    def __init__(self):
        self.directories = [
            "src/constants",
            "config",
            "src/agents",
            "src/llm",
            "src/utils",
            "src/tasks",
            "src/schemas",
            "src/tools",
            "src/crew",
            "src/app",
            "outs",
        ]

        self.files = [
            "src/__init__.py",
            "src/agents/__init__.py",
            "src/agents/agent.py",
            "src/constants/constant.py",
            "src/constants/__init__.py",
            "src/utils/__init__.py",
            "src/utils/helper.py",
            "src/llm/__init__.py",
            "src/llm/model.py",
            "src/tasks/__init__.py",
            "src/tasks/task.py",
            "src/schemas/__init__.py",
            "src/schemas/schema.py",
            "src/tools/__init__.py",
            "src/tools/tool.py",
            "config/agent_param.yaml",
            "config/task_param.yaml",
            "outs/search_queries_agent.json",
            "outs/search_engine_agent.json",
            "outs/scraping_agent.json",
            "outs/reporter_agent.html",
            "src/crew/__init__.py",
            "src/crew/define.py",
            "src/crew/main.py",
            "src/app/__init__.py",
            "src/app/interface.py",
            ".env",
            ".gitignore",
            "README.md",
            "LICENSE",
            "requirements.txt",
        ]
