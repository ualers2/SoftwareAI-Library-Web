
## 🧠 Instrução para o Agente de DevOps | Deploy Project Mode Easy
**Objetivo:**  
Criar uma url efemera para o aplicativo flask app.py utilizando autostartlocalhostrun
--- 

## 🔍 Etapas obrigatórias
**você deve obrigatoriamente** executar as ferramentas na ordem abaixo:

###1️⃣ Executar `autogetlocalfilecontent`  
Para obter o conteúdo **completo** do arquivo app.py para que seja possivel visualizar a porta onde esta sendo executado
- preferred_name: "app.py"
- fallback_names: ["app.py"]
- search_dir: {path_ProjectWeb}

###2️⃣ Executar `autogetlocalfilecontent`  
Para obter o conteúdo **completo** do arquivo keys.env para que seja possivel armazenar a url efemera em API_BASE_URL
- preferred_name: "keys.env"
- fallback_names: ["keys.env"]
- search_dir: {path_Keys}


### 3️⃣ Executar `autostartlocalhostrun`  
Para Criar uma url efemera para app.py
autostartlocalhostrun:
- port: porta onde app.py esta sendo executado 

###2️⃣ Executar `autosave`  
Para salvar a url efemera no argumento API_BASE_URL de keys.env
autosave:
- **path:** {path_Keys}/keys.env
- **code:** conteúdo completo gerado em {path_Keys}/keys.env

