FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install openai-agents
RUN pip install --no-cache-dir --upgrade softwareai-engine-library
 # Para Debian/Ubuntu
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copiar todos os arquivos do projeto
COPY . /app


