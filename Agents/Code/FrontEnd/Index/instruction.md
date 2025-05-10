## 🚀 Instrução Profissional para Geração de Landing Page Com base no pre planejamento

## 🎯 Objetivo
Criar um **único arquivo `index.html`** com base no conteudo de preplanejamento.md contendo:
- NÃO CRIAR LANDINPAGES QUE NAO REFLETEM O CONTEUDO DE preplanejamento.md 
- NAO CRIAR LANDINGPAGE FORA DO QUE FOI SOLICITADO NO CONTEUDO DE preplanejamento.md 
- Estrutura semântica e acessível com **HTML5**
- Estilo coeso, sofisticado e leve utilizando **CSS embutido**
- Funcionalidades interativas em **JavaScript puro**, entregando uma **experiência fluida e envolvente**

---

## 🧰 Ferramentas Disponíveis
Quando gerar index.html, você tem acesso às ferramentas `autosave`, que **devem ser usadas obrigatoriamente** para o salvamento do arquivo criado
### 📥 autosave
- **path:** {path_html}/index.html
- **code:** conteúdo completo gerado

## 🔍 Etapas obrigatórias antes da Codificacao
Antes de começar a escrever qualquer codigo, **você deve obrigatoriamente** executar as ferramentas na ordem abaixo:
### 1️⃣ Executar `autogetlocalfilecontent`  
Para obter o esta previsto em ``### Componentes da Landing Page`` para que seja possivel o desenvolvimento do index.html
autogetlocalfilecontent:
- preferred_name: "preplanejamento.md"
- fallback_names: ["preplanejamento.md", "planejamento.md", "plano.md"]
- search_dir: {doc_md}


---

## 🧱 Especificações Técnicas Obrigatórias
### 🔹 Arquitetura
- Documento único: **HTML, CSS e JS juntos no mesmo arquivo**
- Layout completo com seções clássicas de alta conversão:
- `header` (navegação)
- `hero` (apresentação principal)
- `features` (recursos ou benefícios)
- `pricing` (planos ou ofertas)
- `testimonials` (depoimentos)
- `faq` (perguntas frequentes com acordeões)
- `cta` (chamada para ação)
- `footer` (rodapé com links e informações)
- Navegação com **scroll suave**, menu mobile funcional, efeitos sutis de interação e UX intuitiva
- **Design limpo, profissional, responsivo e de carregamento rápido**

---

## 🔹 Estrutura base (`index.html`)
Utilize o esqueleto abaixo como base, mantendo todas as instruções:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title><!-- título da landing --></title>
<meta name="description" content="<!-- descrição curta da landing -->">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* 🎨 CSS BASE: reset, tipografia, variáveis globais e utilidades */
:root {{
  --primary: #8B5CF6;
  --primary-light: #A78BFA;
  --primary-dark: #7C3AED;
  --primary-gradient: linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%);
  --secondary: #1E293B;
  --background: #F8FAFC;
  --background-alt: #F1F5F9;
  --text: #1E293B;
  --text-light: #64748B;
  --white: #FFFFFF;
  --border: #E2E8F0;
  --success: #10B981;
  --error: #EF4444;
  --warning: #F59E0B;
  --info: #3B82F6;
  --radius: 8px;
  --shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
  --transition: all 0.3s ease;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: 'Inter', system-ui, sans-serif;
  line-height: 1.6;
  color: var(--text);
  background: var(--background);
}}
a {{ text-decoration: none; color: var(--text); transition: var(--transition); }}
ul {{ list-style: none; }}
.container {{
  width: 100%; max-width: 1200px;
  margin: 0 auto; padding: 0 1.5rem;
}}
h1,h2,h3,h4,h5,h6 {{ font-weight: 700; line-height: 1.2; margin-bottom: 1rem; }}
h1{{font-size: 3rem;}} h2{{font-size: 2.25rem;}} h3{{font-size: 1.5rem;}}
p{{margin-bottom: 1rem; color: var(--text-light);}}
.btn {{
  display: inline-block; padding: .75rem 1.5rem;
  border-radius: var(--radius); font-weight: 500;
  cursor: pointer; transition: var(--transition); text-align: center;
}}
.btn-primary {{
  background: var(--primary-gradient); color: var(--white); border: none;
}}
.btn-primary:hover {{
  box-shadow: 0 4px 12px rgba(139,92,246,0.3);
  transform: translateY(-1px);
}}
.btn-outline {{
  background: transparent; color: var(--primary);
  border: 1px solid var(--primary);
}}
.btn-outline:hover {{
  background: rgba(139,92,246,0.1);
}}
.btn-text {{
  background: transparent; color: var(--primary);
  padding: .75rem 0;
}}
.btn-text:hover {{ text-decoration: underline; }}
.btn-large {{ padding: 1rem 2rem; font-size: 1.125rem; }}
.btn-full {{ width: 100%; }}
/* 🔧 Estilos adicionais e seções personalizadas devem ser definidos abaixo */
</style>
</head>
<body>
<header class="header"><div class="container"><nav class="navbar"><!-- logo, links e botão CTA --></nav></div></header>
<main>
<section class="hero">…</section>
<section id="features" class="features">…</section>
<section id="pricing" class="pricing">…</section>
<section class="features-grid">…</section>
<section id="testimonials" class="testimonials">…</section>
<section id="faq" class="faq">…</section>
<section class="cta">…</section>
</main>
<footer class="footer">…</footer>
<script>
// 🔧 Funcionalidades em JavaScript:
// - menu mobile responsivo
// - rolagem suave entre seções
// - botão "voltar ao topo"
// - accordions interativos na seção FAQ
// - slider/carrossel para depoimentos
</script>
</body>
</html>
```

---

## 🔑 Regras Essenciais

✅ HTML, CSS e JS em um **único arquivo autossuficiente**  
✅ **Design responsivo e contemporâneo**, com foco em conversão  
✅ **Experiência fluida** com interações animadas e responsivas  
✅ **Sem frameworks externos** (como Bootstrap ou jQuery)  
✅ **Fonte Inter** já configurada via Google Fonts  
✅ Nenhum uso de `inline styles` ou `onclick`  
✅ Arquitetura limpa, organizada e fácil de escalar  
✅ **CSS Base completo** acima de qualquer estilo de componente  
