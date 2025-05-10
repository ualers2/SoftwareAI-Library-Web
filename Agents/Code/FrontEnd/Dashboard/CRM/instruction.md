
## 🧠 Instrução Profissional para Geração da Seção de CRM (Customer Relationship Manager)

## 🎯 Objetivo

Adicionar uma nova **seção funcional ao painel** já existente no `dashboard.html`, dedicada ao gerenciamento de leads, oportunidades, clientes e funil de vendas.

---

## 🧰 Ferramentas Disponíveis

Você pode usar a ferramenta `autosave`, obrigatoriamente, para salvar o arquivo gerado.  
### 📥 autosave
- **path:** `{path_html}/dashboard.html`
- **code:** conteúdo completo gerado em `{path_html}/dashboard.html`

---

## 🔍 Etapas obrigatórias antes da codificação 

### 1️⃣ Executar `autogetlocalfilecontent`
autogetlocalfilecontent:
  preferred_name: "index.html"
  fallback_names: ["index.html"]
  search_dir: {path_html}

⚠️ O painel deve refletir **exatamente os recursos de <!-- Features Section --> em `index.html`**.

---

## 🧱 Estrutura Esperada das Seçoes

  -🧩 **Menu lateral - 🔍 Funil de Vendas Visual** 
        Ao clicar na opção "Funil de Vendas Visual" no menu lateral, a área `main` deve ser atualizada dinamicamente com os seguintes elementos reais (sem placeholders ou alertas):

        1. Resumo com Cards Dinâmicos
        Objetivo: Mostrar KPIs de vendas (ex: Total de Leads, Em Negociação, Convertidos, Perdidos) com contagem atualizada automaticamente com base nos dados.

        HTML Base:
{ResumocomCardsDinâmicos_HTML}
        JavaScript Base:
{ResumocomCardsDinâmicos_JavaScript}
        CSS Base:
{ResumocomCardsDinâmicos_CSS}
        2. Kanban Interativo (Drag and Drop)
        Objetivo: Exibir os leads em colunas por etapa do funil e permitir movimentação entre colunas via drag and drop.

        HTML Base:
{KanbanInterativo_HTML}
        JavaScript Base:
{KanbanInterativo_JavaScript}
        CSS Base:
{KanbanInterativo_CSS}
        3. Cadastro de Lead (Modal)
        Objetivo: Permitir o cadastro imediato de um novo lead com nome e etapa inicial.

        HTML Base:
{CadastrodeLead_HTML}
        JavaScript Base:
{CadastrodeLead_JavaScript}
        CSS Base:
{CadastrodeLead_CSS}
        4. Tabela de Clientes (Fechados)
        Objetivo: Exibir leads convertidos em formato tabular com valor, data e botão de ação.

        HTML Base:
{TabeladeClientes_HTML}
        JavaScript Base:
{TabeladeClientes_JavaScript}
  -🧩 **Menu lateral - 🎯 Gestão de Clientes** 
        1. Indicadores Dinâmicos
        Objetivo: Exibir KPIs de clientes (Total, Ativos, Inativos, Último Adicionado) com atualização em tempo real.

        HTML Base:
{IndicadoresDinâmicos_HTML}
        JavaScript Base:
{IndicadoresDinâmicos_JavaScript}
        CSS Base:
            /* Pode reaproveitar a mesma definição de .summary-container e .summary-card da seção anterior */

        2. Tabela Detalhada
        Objetivo: Listar todos os clientes com campos completos e ações funcionais.

        HTML Base:
{TabelaDetalhada_HTML}
        JavaScript Base:
{TabelaDetalhada_JavaScript}
    
        3. Cadastro de Cliente (Modal)
        Objetivo: Permitir adicionar clientes completos com nome, e-mail, telefone e status.

        HTML Base:
{CadastrodeCliente_HTML}
        JavaScript Base:
{CadastrodeCliente_JavaScript}
        CSS Base:
            /* Reaproveita o CSS da modal da seção anterior */

        4. Ações de Edição, Exclusão e Histórico
        Objetivo: Permitir gerenciamento total do cliente via botões da tabela.

        JavaScript Base:
{AçõesdeEdiçãoExclusãoeHistórico_JavaScript}
  -🧩 **Menu lateral - 🧰 Automação de Follow-ups 
        Objetivo Geral: Automatizar interações pós-contato com leads/clientes, garantindo lembretes visuais, envio automático de follow-ups por e-mail, e gestão eficiente de pendências — sem recarregar a página.

        1. Lista de Follow-ups Agendados
        Objetivo: Exibir todos os follow-ups programados com status e ações imediatas.

        HTML Base:
{ListadeFollowupsAgendados_HTML}

        JavaScript Base:
{ListadeFollowupsAgendados_JavaScript}
        2. Formulário para Agendar Novo Follow-up
        Objetivo: Criar novos follow-ups com informações reais (nome, e-mail, data agendada, mensagem).

        HTML Base:
{FormulárioparaAgendarNovoFollowup_HTML}

        JavaScript Base:
{FormulárioparaAgendarNovoFollowup_JavaScript}

        3. Envio Simulado de E-mail (Apenas para apresentação inicial do painel)
        Obs: Em ambiente real, o envio seria feito por backend. Aqui, simulamos a ação visual e atualizamos o status.
        JavaScript Base:
{EnvioSimuladodeEmail_JavaScript}
        4. Cancelamento de Follow-up
        JavaScript Base:
{CancelamentodeFollowup_JavaScript}
        5. Disparador de Agendamentos (Intervalo Simulado)
        Verifica a cada minuto se algum follow-up está agendado para o horário atual (ou anterior) e envia automaticamente.
        JavaScript Base:
{DisparadordeAgendamentos_JavaScript}
        6. Estilo (CSS)
        CSS Base:
{AutomaçãodeFollowups_CSS}
  -🧩 **Menu lateral - 📊 Seção: Relatórios e Metas
        
        Objetivo Geral: Permitir análise clara e visual do desempenho da equipe com indicadores, gráficos interativos, e gestão de metas por período, tudo com atualização dinâmica e sem recarregar a página.

        1. Indicadores-Chave de Performance (KPIs)
        Objetivo: Mostrar rapidamente os principais números (ex: vendas totais, metas batidas, taxa de conversão).

        HTML Base:
{IndicadoresChavedePerformance_HTML}
        JavaScript Base:
{IndicadoresChavedePerformance_JavaScript}
        2. Gráfico de Desempenho Mensal (Canvas)
        Objetivo: Exibir um gráfico de barras com vendas por mês.

        JavaScript Base:
{GráficodeDesempenhoMensal_JavaScript}
        3. Tabela de Metas por Colaborador
        Objetivo: Mostrar metas por colaborador com progresso percentual e ações.

        HTML Base:
{TabeladeMetasporColaborador_HTML}

        JavaScript Base:
{TabeladeMetasporColaborador_JavaScript}

        4. Estilo (CSS)
        CSS Base para indicadores e layout:
{SeçãoRelatórioseMetas_CSS}

