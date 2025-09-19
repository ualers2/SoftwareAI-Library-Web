import os
import io
import zipfile
import time
import requests
import importlib.util
from flask import Flask, request, jsonify, make_response
# Diretórios raiz onde agentes podem estar
BASE_DIR = os.path.dirname(__file__)
AGENTS_DIR = ['AgentsDownloaded']  # pasta onde ZIP é extraído

def download_agents_zip(agent_ids: list, extract_dir=None) -> bool:
    """
    Faz o download do ZIP contendo os arquivos .py de múltiplos agentes.
    Após o download, extrai para a pasta de agentes especificada.

    :param agent_ids: Lista com os IDs dos agentes.
    :param extract_dir: Diretório onde o ZIP será extraído.
    :return: True se tudo foi bem-sucedido, False caso contrário.
    """
    extract_dir = extract_dir or os.path.join(os.path.dirname(__file__), 'AgentsDownloaded')
    output_path = 'agents_code.zip'
    base_url = 'https://softwareai-library-hub.rshare.io'
    joined_ids = ','.join(agent_ids)
    url = f'{base_url}/api/agent-code/{joined_ids}'

    for attempt in range(1, 11):
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(resp.content)

                os.makedirs(extract_dir, exist_ok=True)
                with zipfile.ZipFile(output_path, 'r') as zf:
                    zf.extractall(extract_dir)

                os.remove(output_path)
                return True
            else:
                print(f"Tentativa {attempt}: Código {resp.status_code} - {resp.text}")
        except Exception as e:
            print(f"Erro na tentativa {attempt}: {e}")
        time.sleep(5)
    return False

def import_agent(agent_name: str, base_dir=None):
    base_dir = base_dir or os.path.join(BASE_DIR, 'AgentsDownloaded')
    # Procura recursivamente o Integration.py dentro de pastas que terminam com o agent_name
    module_path = None
    for dirpath, _, filenames in os.walk(base_dir):
        if os.path.basename(dirpath) == agent_name and 'Integration.py' in filenames:
            module_path = os.path.join(dirpath, 'Integration.py')
            break
    if not module_path:
        raise ImportError(f"Integration.py não encontrado para agente '{agent_name}'")

    # Importa módulo dinâmico
    spec = importlib.util.spec_from_file_location(agent_name, module_path)
    if not spec or not spec.loader:
        raise ImportError(f"Falha ao criar spec para '{module_path}'")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Busca classe que termina com 'Agent'
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and attr_name.endswith('Agent'):
            return attr
    raise ImportError(f"Nenhuma classe Agent encontrada em '{module_path}'")


def EgetAgents(agent_list=None):
    """
    Baixa e importa dinamicamente múltiplos agentes.
    :param agent_list: Lista de nomes de agentes.
    :return: Lista de classes de agentes.
    """
    agents = agent_list or []
    success = download_agents_zip(agents)
    if not success:
        raise RuntimeError("Falha ao baixar pacotes de agentes")

    imported = []
    for ag in agents:
        imported.append(import_agent(ag))
    return imported

imported = EgetAgents(agent_list=["PreProject", 
                                   "Timeline", 
                                   "Dashboard_Decision", 
                                   "TypeProject"
                                ])

