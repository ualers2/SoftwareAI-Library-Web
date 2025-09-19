from agents import Agent, handoff, RunContextWrapper
import json
import re
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel

path_ProjectWeb = "/app/LocalProject"
# os.chdir(path_ProjectWeb)
path_html = f"{path_ProjectWeb}/templates"
path_js = f"{path_ProjectWeb}/static/js"
path_css = f"{path_ProjectWeb}/static/css"
doc_md = f"{path_ProjectWeb}/doc_md"

path_metadata = os.path.join(os.path.dirname(__file__), "metadata.json")
with open(path_metadata, encoding='utf-8') as f:
    metadata = json.load(f)
    instruction_property = metadata.get("instruction_property")
    instruction = metadata.get("instruction")
    model_agent = metadata.get("model")
    tools_agent = metadata.get("tools")
    name_agent = metadata.get("name")
    # Extrair valor de path_html da string no campo instruction_property
    prop_str = metadata['instruction_property']['path_html']


path_instruction = os.path.join(os.path.dirname(__file__), "instruction.md")
with open(path_instruction, 'r', encoding='utf-8') as f:
    instruction_original = f.read()


instruction_formatado = instruction_original.replace('{path_html}', prop_str)

print(instruction_formatado)