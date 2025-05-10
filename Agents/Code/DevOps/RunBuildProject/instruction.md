
Ao final de sua execução, utilize o Handoffs 
---

## 🧠 Instrução para o Agente de Run Build Project
**Objetivo:**  
Executar autobuildconteinerwithcompose para rodar o projeto localmente construindo o conteiner docker 

--- 

## 🔍 Etapas obrigatórias para rodar o projet
Antes de começar a escrever qualquer código ou modificar arquivos, **você deve obrigatoriamente** executar as ferramentas na ordem abaixo:
### 1️⃣ Executar `autobuildconteinerwithcompose`  
Para que seja possivel construir o conteiner docker
autobuildconteinerwithcompose:
- compose_file: "{path_ProjectWeb}/docker-compose.yml"
- service_name: landingpage
- wait_for: "running"
- healthcheck: False
- timeout: 300
