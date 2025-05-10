

## 🧠 Instrução para o Agente de Integração Backend Flask

**Objetivo:**  
Criar os **endpoints iniciais** de navegação da aplicação Flask, que servirão as páginas principais do sistema: landing page, login, checkout, e páginas de resultado do checkout.

---

## 🧰 Ferramentas Disponíveis

Quando gerar os arquivos esperados, você tem acesso às ferramentas `autosave`, que **devem ser usadas obrigatoriamente** para o salvamento do arquivo app.py criado 
### 📥 autosave
- **path:** app.py
- **code:** conteúdo completo gerado em app.py

---

## 🔍 Etapas obrigatórias antes da codificação
Antes de começar a escrever qualquer código ou modificar arquivos, **você deve obrigatoriamente** executar as ferramentas na ordem abaixo:
### 1️⃣ Executar `autogetlocalfilecontent`  
Para obter o conteúdo **completo** do arquivo index para que seja possivel o desenvolvimento das modificacoes
autogetlocalfilecontent:
- preferred_name: "index.html"
- fallback_names: ["index.html"]
- search_dir: {path_html}

---

### 2️⃣ Executar `autogetlocalfilecontent`  
Para obter o conteúdo **completo** do arquivo cronograma para que seja possivel visualizar os codigos base fornecidos para os endpoints criticos
autogetlocalfilecontent:
- preferred_name: "cronograma.md"
- fallback_names: ["cronograma.md"]
- search_dir: {doc_md}

---

## 🌐 Codigo base Validado como ponto de partida para iniciacao da api:
```python
{basic_endpoints}
```

## 🌐 Endpoints esperados:
**Objetivo:** Integrar endpoints basicos no arquivo ``app.py``
**Tarefas:**
- endpoint `/` que leva a `templates/index.html`
- endpoint `/login` que leva ao templates/login.html 
- endpoint `/checkout` que leva ao templates/checkout.html
- endpoint `/checkout/sucess` que leva ao templates/success.html


---

## 🧩 Regras Técnicas

- Utilizar Flask puro (`from flask import Flask, render_template`)
- Todos os endpoints devem usar `@app.route()`
- As views devem retornar `render_template()` com o caminho correto para os arquivos HTML
- Não criar lógica extra ou autenticação — foco apenas nos endpoints básicos
- Todos os endpoints devem estar acessíveis via navegador
- Renders devem apontar corretamente para os templates existentes
- Sem lógica adicional ou verificação de login/autenticação
- Código limpo e bem identado

