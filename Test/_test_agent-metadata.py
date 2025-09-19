import requests
from agents import Agent,Runner, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel
from firebase_admin import credentials, initialize_app, db







from modules.Egetoolsv2 import *
from modules.EgetMetadataAgent import *

dotenv_path= os.path.join(os.path.dirname(__file__), "keys.env")
load_dotenv(dotenv_path=dotenv_path)
# session_id_CodePreProject = "teste_handoff_CodePreProject"

# path_APPCOMPANY = r"D:\CompanyApps\Projetos de codigo aberto\SoftwareAIEngine\EngineEndpointAgentAPI\Library\web\Agents\CodePreProject\Keys\appcompany.json" #"/app/Keys/appcompany.json"
# with open(path_APPCOMPANY) as f:
#     firebase_credentials_APPCOMPANY = json.load(f)

# credt1 = credentials.Certificate(firebase_credentials_APPCOMPANY)
# appcompany = initialize_app(credt1, {
#    'storageBucket': 'aicompanydata1.appspot.com',
#    'databaseURL': 'https://aicompanydata1-default-rtdb.europe-west1.firebasedatabase.app'
# }, name='appcompany')



def main():
    user_message = """
Quero um site para meu saas de ia 
    """

    print("🧠 Enviando mensagem ao agente ...")

    # path_ProjectWeb = r"D:\CompanyApps\Projetos de codigo aberto\SoftwareAIEngine\EngineEndpointAgentAPI\Library\web\Agents\meu_handoff_projeto\LocalProject"
    # os.chdir(path_ProjectWeb)
    # path_html = "templates"
    # path_js = "static/js"
    # path_css = "static/css"
    # doc_md = "doc_md"

    agent_ids = ['PreProject']
    agents_metadata = EgetMetadataAgent(agent_ids)

    name_PreProject = agents_metadata['PreProject']["name"]
    model_PreProject = agents_metadata['PreProject']["model"]
    instruction_PreProject = agents_metadata['PreProject']["instruction"]
    tools_PreProject = agents_metadata['PreProject']["tools"]

    Tools_Name_dict = Egetoolsv2(list(tools_PreProject))
    agent = Agent(
        name=str(name_PreProject),
        instructions=str(instruction_PreProject),
        model=str(model_PreProject),
        tools=Tools_Name_dict

    )

    result = Runner.run_sync(agent, user_message)
    
    # A resposta final do agente fica em result.final_output
    print(f"🤖 Resposta do sistema:\n{result.final_output}")

if __name__ == "__main__":
    main()
