# SoftwareAI Engine


### Release v1.0.19
#### objetivo alcançado: Funcoes da biblioteca 100% operacionais para agentes construidos com o sdk de agentes openai

- [x] https://softwareai-library-hub.rshare.io/tools: agora é possivel ver o codigo fonte da function tool ao clickar em `View function tool and metadata`
- [x] https://softwareai-library-hub.rshare.io/tools: ajustado o metadata 

- [x] softwareai_engine_library: agora é possivel buscar as funcoes disponiveis atraves de api da biblioteca segue exemplo:
##### primeiro obtenha as funcoes hospedadas na biblioteca
```python
from softwareai_engine_library.EngineProcess.EgetTools import Egetoolsv2
imported_tools = Egetoolsv2(functionstools = ['autosave', 'autobuildpdf'])

```
##### tenha em mente que imported_tools é uma lista de functions tools pronta para ir para tools
```python

def run_sync(agent, input):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(Runner.run(agent, input=input))

agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    model="o3-mini",
    tools=imported_tools,
)
result = run_sync(agent, input="Escreva um codigo python e salve em D:/CompanyApps/Projetos de codigo aberto/SoftwareAIEngine/EngineEndpointAgentAPI/Library/Agents/CodePreProject/Tests/docs/teste.py.")
print(result.final_output)
```


