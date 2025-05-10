 # Pull Request: Novas Ferramentas e Atualização de Agentes

 ## 🧰 Contexto
 Este PR adiciona duas novas ferramentas de build de container e registra a introdução de um novo agente de Code Review. Também atualiza diversos agentes existentes para suportar melhor os fluxos de DevOps e CI/CD.

 ---

 ## ✨ Novas Tools
- **autobuildContainerWithCompose**  
  Automatiza o build de containers usando Docker Compose, detectando alterações em `docker-compose.yml` e reiniciando os serviços conforme necessário.

- **autobuildContainer**  
  Realiza o build e deploy de uma imagem Docker a partir do `Dockerfile` raiz do projeto, empurrando automaticamente para o registry configurado.

 ---

 ## 🤖 Novo Agente de Code Review
- **CodeReview_DevOps_Docker**  
  Especializado em práticas de containerização, otimização de imagens Docker, qualidade de `Dockerfile` e orquestração via Compose/Kubernetes.

 ---

 ## 🔧 Agentes Existentes Modificados
- CodeReview_BackEnd_Endpoints  
- CodeReview_FrontEnd_Html  
- CodeReview_Preproject  
- CodeReview_Timeline  
- DeployProjectModeEasy  
- RunBuildProject  
- Checkout  
- Dashboard  
- Index  
- Login  
- CreateWebhook  
- Modules  
- Staticjs  
- Technich  
- Keys_env  
- Timeline  

 _As mudanças nessas classes incluem melhorias de logging, tratamento de erros mais robusto e compatibilidade com as novas ferramentas de container._

 ---

 ## 🧪 Como Testar
1. Faça checkout nesta branch:  
   ```bash
   git fetch origin && git checkout feature/new-container-tools
   ```
2. Instale dependências e prepare o ambiente:  
   ```bash
   npm install         # ou pip install -r requirements.txt
   ```
3. Execute os pipelines de CI localmente para validar os agentes:  
   ```bash
   npm run test        # ou pytest
   ```
4. Teste as novas tools de build de container:  
   ```bash
   # Teste do compose
   autobuildContainerWithCompose --up  
   
   # Teste do build simples
   autobuildContainer --build
   ```
5. Execute o agente de Code Review Docker:  
   ```bash
   codex run-agent CodeReview_DevOps_Docker --target ./Dockerfile
   ```

 ---

 ## 📄 Documentação Atualizada
- Adicionei exemplos de uso de `autobuildContainerWithCompose` e `autobuildContainer` em `docs/devops/docker-tools.md`.
- Atualizei o README com a lista completa de agentes suportados.

 ---

 ## 📋 Checklist
- [ ] Ferramentas testadas localmente  
- [ ] Agentes de Code Review executados sem erros  
- [ ] Documentação atualizada  
- [ ] Todos os testes unitários passam  