"""
DevTechBytes
https://www.youtube.com/@DevTechBytes
"""
# https://python.langchain.com/docs/integrations/llms/ollama/
from langchain_community.llms import Ollama
# https://github.com/ollama/ollama/blob/main/docs/README.md
from config import Config

import ollama

def get_models():
    ...

def get_system_prompt():
    ...

def chat(user_prompt, model):
    ...

