from template.structure import ProjectStructure
from src.constants.constant import *
from pathlib import Path
import logging
import sys
import os


class ProjectSetup:
    def __init__(self, log_dir=LOG_DIR):
        self.log_dir = Path(log_dir)
        self.setup_logging()
        self.logger = logging.getLogger(__name__)
        self.structure = ProjectStructure()

    def setup_logging(self):
        self.log_dir.mkdir(exist_ok=True)
        log_file = os.path.join(LOG_DIR, LOG_FILE)

        logging.basicConfig(
            level=logging.INFO,
            format=LOGGING_FORMAT,
            datefmt=DATEFMT,
            handlers=[logging.FileHandler(log_file), logging.StreamHandler(sys.stdout)],
        )

    def create_directory(self, path: Path):
        try:
            if path.exists():
                self.logger.info(f"Directory already exists: {path}")
            else:
                os.makedirs(path, exist_ok=True)
                self.logger.info(f"Created directory: {path}")

        except OSError as e:
            self.logger.error(f"Error creating directory {path}: {e}")
            raise

    def create_file(self, path: Path):
        try:
            if path.exists():
                self.logger.info(f"File already exists: {path}")
            else:
                path.touch(exist_ok=True)
                self.logger.info(f"Created file: {path}")

        except OSError as e:
            self.logger.error(f"Error creating file {path}: {e}")
            raise

    def create_structure(self):
        for dir_path_str in self.structure.directories:
            self.create_directory(Path(dir_path_str))

        for file_path_str in self.structure.files:
            file_path = Path(file_path_str)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            self.create_file(file_path)
