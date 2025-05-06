from setuptools import find_namespace_packages, setup
from src.constants.constant import *

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_namespace_packages(include=["src", "template"]),
)
