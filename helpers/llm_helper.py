"""
Orignal Author: DevTechBytes
https://www.youtube.com/@DevTechBytes
"""
# https://python.langchain.com/docs/integrations/llms/ollama/
from langchain_community.llms import Ollama
from config import Config
import ollama 
system_prompt = Config.SYSTEM_PROMPT

def get_models():
    # tuple to hold models
    models = () 

    # loops through list of ollama models on computer
    for model in ollama.list()['models']:
        models += (model['name'],)  # Append the model's name to the tuple

    return models

def get_system_prompt():
    system_prompt = f"""You are a helpful chatbot that has access to the following 
                    open-source models {get_models()}.
                    You can can answer questions for users on any topic."""
    
    return system_prompt

def chat(user_prompt, model):
    # instantiate Ollama model using langchain
    llm = Ollama(model=model, system=get_system_prompt())

    # streams back response to UI
    for chunk in llm.stream(f"Model being used: {model} {user_prompt}"):
        yield chunk

