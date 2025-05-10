#########################################
# IMPORT SoftwareAI Libs 
from softwareai_engine_library.Inicializer._init_libs_ import *
#########################################
# IMPORT SoftwareAI Core
from softwareai_engine_library.Inicializer._init_core_ import *
#########################################
import subprocess
import docker
import time
import logging
from typing_extensions import TypedDict, Literal
from agents import function_tool

# Configuração do logger
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
    return logger

class DockerComposeData(TypedDict):
    compose_file: str          ## Caminho para o arquivo docker-compose.yml
    service_name: str          # Nome do serviço definido no compose a iniciar
    wait_for: Literal['running', 'healthy']
    healthcheck: bool          # Se True, espera HEALTHCHECK (requer healthcheck no compose)
    timeout: int               # Timeout em segundos para espera

@function_tool
def autobuildconteinerwithcompose(data: DockerComposeData):
    logger = get_logger(__name__)
    try:
        compose_file = data['compose_file']
        service = data['service_name']
        wait_for = data.get('wait_for', 'running')
        healthcheck = data.get('healthcheck', False)
        timeout = data.get('timeout', 120)

        # 1) Build do compose
        logger.info(f"Building services in '{compose_file}'...")
        subprocess.run([
            'docker-compose', '-f', compose_file, 'build', service
        ], check=True)

        # 2) Up do serviço em modo destacado
        logger.info(f"Starting service '{service}'...")
        subprocess.run([
            'docker-compose', '-f', compose_file, 'up', '-d', service
        ], check=True)

        # 3) Aguardar condição via SDK
        client = docker.from_env()
        container = None
        # localizar container pelo nome padrão: compose proj_service_1
        project = subprocess.run([
            'docker-compose', '-f', compose_file, 'ps', '-q', service
        ], capture_output=True, text=True, check=True).stdout.strip()
        if project:
            container = client.containers.get(project)
        else:
            raise RuntimeError(f"Não encontrou container para serviço '{service}'.")

        start = time.time()
        logger.info(f"Waiting for container '{service}' status '{wait_for}' (timeout={timeout}s)...")
        while True:
            container.reload()
            status = container.status
            if healthcheck and wait_for == 'healthy':
                state = container.attrs.get('State', {})
                health = state.get('Health', {}).get('Status')
                logger.info(f"Health status: {health}")
                if health == 'healthy':
                    break
            else:
                logger.info(f"Current status: {status}")
                if status == wait_for:
                    break

            if time.time() - start > timeout:
                raise TimeoutError(f"Timeout waiting for '{service}' to be {wait_for}.")
            time.sleep(2)

        logger.info(f"Service '{service}' is now {wait_for}.")
        return {"status": "success", "message": f"Service '{service}' ready (status={wait_for})."}

    except Exception as e:
        logger.error(f"Erro na execução de compose: {e}")
        return {"status": "error", "message": str(e)}
