#########################################
# IMPORT SoftwareAI Libs 
from softwareai_engine_library.Inicializer._init_libs_ import *
#########################################
# IMPORT SoftwareAI Core
from softwareai_engine_library.Inicializer._init_core_ import *
#########################################
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

class DockerData(TypedDict):
    build_path: str           # Caminho para o contexto de build (ex: '.')
    image_tag: str            # Tag da imagem (ex: 'meu-app:latest')
    container_name: str       # Nome do container a ser criado
    run_command: list[str]    # Comando e args para rodar no container (ex: ['python', 'app.py'])
    wait_for: Literal['running', 'healthy']
    healthcheck: bool         # Se True, espera até healthy (requer HEALTHCHECK no Dockerfile)
    timeout: int              # Timeout em segundos para espera

@function_tool
def autobuildconteiner(data: DockerData):
    logger = get_logger(__name__)
    try:
        # Extrair parâmetros
        path = data['build_path']
        tag = data['image_tag']
        name = data['container_name']
        cmd = data['run_command']
        wait_for = data.get('wait_for', 'running')
        healthcheck = data.get('healthcheck', False)
        timeout = data.get('timeout', 120)

        logger.info(f"Building image '{tag}' from '{path}'...")
        client = docker.from_env()

        # 1) Build da imagem
        image, build_logs = client.images.build(path=path, tag=tag)
        for chunk in build_logs:
            if 'stream' in chunk:
                logger.info(chunk['stream'].strip())

        # 2) Rodar o container em modo destacado
        logger.info(f"Creating and starting container '{name}'...")
        container = client.containers.run(
            tag,
            name=name,
            command=cmd,
            detach=True
        )

        # 3) Esperar pela condição
        start = time.time()
        logger.info(f"Waiting for container status '{wait_for}' (timeout={timeout}s)...")
        while True:
            container.reload()
            status = container.status
            if healthcheck and wait_for == 'healthy':
                state = container.attrs.get('State', {})
                health = state.get('Health', {}).get('Status')
                logger.info(f"Health status: {health}")
                if health == 'healthy': break
            else:
                logger.info(f"Current status: {status}")
                if status == wait_for: break

            if time.time() - start > timeout:
                raise TimeoutError(f"Timeout waiting for container '{name}' to be {wait_for}.")
            time.sleep(2)

        logger.info(f"Container '{name}' is now {wait_for}.")
        return {"status": "success", "message": f"Container '{name}' ready (status={wait_for})."}

    except Exception as e:
        logger.error(f"Erro na execução Docker SDK: {e}")
        return {"status": "error", "message": str(e)}
