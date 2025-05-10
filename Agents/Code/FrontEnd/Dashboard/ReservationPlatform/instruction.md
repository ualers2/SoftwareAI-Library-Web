## 🧠 Instrução Profissional para Geração De painel de Plataforma de Reservas 

## 🎯 Objetivo
Criar uma Plataforma de Reservas com Foco em horários, disponibilidade, clientes, pagamentos seguindo os padroes de 🧱 Estrutura Esperada das Seções - Plataforma de Reservas

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

## 🧱 Estrutura Esperada das Seções - Plataforma de Reservas

    ### 🧩 **Menu Lateral - 📅 Agenda Inteligente**
        Ao clicar na opção "Agenda Inteligente" no menu lateral, a área `main` deve ser atualizada dinamicamente com os seguintes elementos reais (sem placeholders ou alertas):

        #### 1. **Calendário Interativo com Slots de Horários**
        **Objetivo:** Exibir uma grade diária ou semanal com horários disponíveis, reservados e ocupados. Permitir cliques para nova reserva.

        **HTML Base:**
            {CalendárioInterativocomSlotsdeHorários_HTML}

        **JavaScript Base:**
            {CalendárioInterativocomSlotsdeHorários_JavaScript}

        **CSS Base:**
            {CalendárioInterativocomSlotsdeHorários_CSS}

        ---

        #### 2. **Resumo de Ocupação (KPIs)**
        **Objetivo:** Exibir indicadores de quantas reservas existem no dia, slots disponíveis e ocupados.

        **HTML Base:**
            {ResumodeOcupação_HTML}

        **JavaScript Base:**
            {ResumodeOcupação_JavaScript}

        ---

        #### 3. **Modal de Nova Reserva**
        **Objetivo:** Capturar nome do cliente, horário e valor pago.

        **HTML Base:**
            {ModaldeNovaReserva_HTML}
        **JavaScript Base:**
            {ModaldeNovaReserva_JavaScript}

        **CSS Base:**
            Reutilizar `.modal`, `.modal-content`, e `.hidden` como no CRM.

        ---

    ### 🧩 **Menu Lateral - 👥 Histórico de Clientes**
        Ao clicar na opção "Histórico de Clientes" no menu lateral, a área `main` deve ser atualizada dinamicamente com os seguintes elementos reais (sem placeholders ou alertas):

        #### 1. **Indicadores de Clientes**
        **Objetivo:** Exibir quantidade total de clientes únicos e último adicionado.

        **HTML Base:**
            {IndicadoresdeClientes_HTML}

        **JavaScript Base:**
            {IndicadoresdeClientes_JavaScript}
        ---

        #### 2. **Tabela de Clientes com Histórico**
        **Objetivo:** Mostrar clientes com número de reservas e total pago.

        **HTML Base:**
            {TabeladeClientescomHistórico_HTML}
        **JavaScript Base:**
            {TabeladeClientescomHistórico_JavaScript}

    ### 🧩 **Menu Lateral - 👥 Histórico de Pagamentos**
        Ao clicar na opção "Histórico de Pagamentos" no menu lateral, a área `main` deve ser atualizada dinamicamente com os seguintes elementos reais (sem placeholders ou alertas):

        #### 3. **Tabela de Pagamentos**
        **Objetivo:** Exibir lista cronológica de reservas feitas com valor e horário.

        **HTML Base:**
            {TabeladePagamentos_HTML}

        **JavaScript Base:**
            {TabeladeClientescomHistórico_JavaScript}
