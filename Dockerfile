FROM python:3.12-slim-bookworm


# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    jq \
    libffi-dev \
    build-essential \
    gcc \
    g++ \
    linux-headers-amd64 \
    libgl1 \
    libssl-dev \
 && rm -rf /var/lib/apt/lists/*
 
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install openai-agents
RUN pip install --no-cache-dir --upgrade softwareai-engine-library

COPY . /app


