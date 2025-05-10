**SoftwareAI Library Web**
Aplicação web construída em Flask que funciona como hub para gerenciar e expor agents e tools da biblioteca SoftwareAI.
![Screenshot_7](https://github.com/user-attachments/assets/d31b9c11-64f7-40a3-9d70-29b523c54562)

---

## Índice

1. [Visão Geral](#visão-geral)
2. [Principais Funcionalidades](#principais-funcionalidades)
3. [Pré-requisitos](#pré-requisitos)
4. [Instalação](#instalação)
5. [Configuração](#configuração)
6. [Como Executar](#como-executar)
7. [Endpoints da API](#endpoints-da-api)
8. [Estrutura do Projeto](#estrutura-do-projeto)
9. [Variáveis de Ambiente](#variáveis-de-ambiente)
10. [Logs](#logs)
11. [Contribuição](#contribuição)
12. [Licença](#licença)

---

## Visão Geral

Este projeto disponibiliza via web um conjunto de serviços para listar, consultar e versionar `agents` e `tools` da biblioteca SoftwareAI. A interface renderiza páginas estáticas e templates em Jinja, enquanto a API RESTful oferece JSON para consumo por frontends ou outros serviços.

## Principais Funcionalidades

* Listagem de agents e tools armazenados no Firebase
* Recuperação de metadados, tutoriais e versões históricas
* Download em ZIP de códigos fonte (Integration.py, metadata.json, .py das tools)
* Exposição de docker-compose YAML do hub
* Sistema de logging configurável
* Suporte a CORS em todas as rotas
* Sessões seguras com tempo de vida configurável

## Endpoints da API

### Páginas HTML

| Rota                       | Método | Descrição                      |
| -------------------------- | ------ | ------------------------------ |
| `/` ou `/index.html`       | GET    | Página inicial                 |
| `/tools` ou `/tools.html`  | GET    | Lista de tools                 |
| `/tools/<tool_id>`         | GET    | Detalhe de uma tool específica |
| `/agents` ou `/agent.html` | GET    | Página de agents               |

### API RESTful

| Rota                                | Método | Descrição                                                         |
| ----------------------------------- | ------ | ----------------------------------------------------------------- |
| `/api/agents`                       | GET    | Lista todos os agents com metadados e status                      |
| `/api/agents/<agent_id>`            | GET    | Retorna tutorial e dados básicos do agent                         |
| `/api/agents/history?agent_id=<id>` | GET    | Histórico de versões do agent, ordenado por timestamp decrescente |
| `/api/compose`                      | GET    | Retorna o arquivo `softwareai-compose.yml`                        |
| `/api/agent-metadata/<ids>`         | GET    | Metadados de um ou múltiplos agents (vírgula-separados)           |
| `/api/tool-metadata/<tool_id>`      | GET    | Metadados e código de uma tool                                    |
| `/api/list-tools`                   | GET    | Lista todas as tools disponíveis                                  |
| `/api/get-tools-by-id`              | POST   | Recebe JSON com `tool_ids` e retorna dados das tools              |
| `/api/tool-code/<tool_ids>`         | GET    | Download em ZIP do código Python de tools especificadas           |
| `/api/agent-code/<agent_ids>`       | GET    | Download em ZIP de Integration.py e metadata.json de agents       |
| `/api/submit-tool-output`           | POST   | Endpoint de callback para submissão de saída de ferramenta        |

## Estrutura do Projeto

```
├── Agents/                       # Diretório de agents locais
├── FunctionsAndTools/           # Ferramentas e funções auxiliares
│   ├── Functions/               # Código das tools
│   └── __init__Functions.py     # Registro das funções
├── Keys/                         # Credenciais e chaves (não versionadas)
├── modules/                      # Módulos internos (load, hash, register)
├── static/                       # Arquivos estáticos (CSS, JS, imagens)
├── templates/                    # Templates Jinja para páginas
├── softwareai-compose.yml       # Compose de demonstração do hub
├── library_hub_app.py           # Aplicação Flask principal
├── requirements.txt             # Dependências Python
└── README.md                     # Este arquivo
```

## Variáveis de Ambiente

* `OPENAI_API_KEY` — chave da API OpenAI
* `FIREBASE_CREDENTIALS` — caminho para JSON de credenciais Firebase
* `FIREBASE_URL` — URL do Realtime Database
* `SECRET_KEY` — chave secreta Flask para sessões

## Logs

O logger `app_logger` está configurado para nível DEBUG e direcionado ao stdout. Formato: `[YYYY-MM-DD HH:MM:SS] LEVEL in module: mensagem`.

## Contribuição

1. Fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request




   
### 🔧 **2. branch `main` seja a principal**

Se o repositório usa `main` como a branch principal, você precisa fazer o commit na `main`, e não na `master`. Para corrigir isso, faça o seguinte:

* **Troque para a branch `main`**:

```bash
git checkout main
```

* **Atualize a branch `main` com as últimas alterações do repositório remoto**:

```bash
git pull origin main
```

* **Volte para a sua branch de trabalho**:

```bash
git checkout master  # ou outra branch de trabalho
```

* **Rebase as alterações na `main`** (ou apenas use `git merge`):

```bash
git rebase main  # ou git merge main
```

* **Suba a branch novamente**:

```bash
git push origin master
```

Agora, você pode tentar criar o PR novamente:

```bash
gh pr create --base main --head master --title "Título do PR" --body "Descrição do PR"
```




## Pré-requisitos

* Python 3.9+
* Docker (opcional, se quiser containerizar)
* Conta e credenciais Firebase
* Chave de API OpenAI válida

## Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/SoftwareAI-Library-Web.git
cd SoftwareAI-Library-Web

# Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

## Configuração

Renomeie o arquivo `.env.example` para `.env` e preencha:

```dotenv
OPENAI_API_KEY=suachaveopenai
FIREBASE_CREDENTIALS=/caminho/para/appcompany.json
FIREBASE_URL=https://seu-projeto.firebaseio.com
SECRET_KEY=uma_chave_secreta_para_sessions
```

## Como Executar

```bash
export FLASK_APP=library_hub_app.py   # ou defina no Windows
export FLASK_ENV=development         # opcional
flask run --host=0.0.0.0 --port=821
```

Ou diretamente:

```bash
python library_hub_app.py
```

Após isso, acesse `http://localhost:821`.

## Licença

MIT © Seu Nome
