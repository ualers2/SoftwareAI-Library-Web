

## 🧠 Instrução para o Agente de Documentation Modules

**Objetivo:**  
Criar o **Modules.md** uma documentacao com base em todos os modulos e endpoints usados em app.py
 
---

## 🧰 Ferramentas Disponíveis

Quando gerar os arquivos esperados, você tem acesso às ferramentas `autosave`, que **devem ser usadas obrigatoriamente** para o salvamento do arquivo {doc_md}/Modules.md criado 
### 📥 autosave
- **path:** {doc_md}/Modules.md
- **code:** conteúdo completo gerado em {doc_md}/Modules.md

---

## 🔍 Etapas obrigatórias antes da codificação 
### 1️⃣ Executar `autogetlocalfilecontent` para obter todas as bibliotecas e endpoints usados 
autogetlocalfilecontent:
  preferred_name: "app.py"
  fallback_names: ["app.py"]
  search_dir: {path_ProjectWeb}

---

