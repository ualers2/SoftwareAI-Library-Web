import requests

# URL da sua API rodando localmente
url = "https://softwareai-library-hub.rshare.io/api/list-tools"

try:
    response = requests.get(url)
    if response.status_code == 200:
        tools = response.json()
        print("Ferramentas encontradas:")
        for tool in tools:
            print(f"- {tool['name']} ({tool['type']})")
    else:
        print(f"Erro {response.status_code}: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar com a API: {e}")
