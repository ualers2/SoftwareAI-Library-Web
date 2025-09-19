import requests
import yaml
import os
import requests

def format_tool(tool):
    return {
        "function": {
            "name": tool["id"],
            "description": tool["fullDescription"],
            "parameters": tool["parameters"]
        },
        
    }

# Simulando carregamento via compose
tools_name_str = "autoapprovepullrequest,autochangesrequestedinpullrequest,autoconversationpullrequest"
tool_ids = [name.strip() for name in tools_name_str.split(',')]

# Pega ferramentas via API
response = requests.post('http://localhost:5000/api/get-tools-by-id', json={"tool_ids": tool_ids})
tools_data = response.json()

# Formata cada ferramenta no formato de função
formatted_tools = [format_tool(tool) for tool in tools_data]
