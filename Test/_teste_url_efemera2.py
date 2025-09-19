from flask import Flask
import threading
import subprocess
import re

def start_localhost_run(port=5000):
    cmd = ['ssh', '-R', '80:127.0.0.1:5000', 'ssh.localhost.run']

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    url = None
    while True:
        line = process.stdout.readline()
        if not line:
            break
        print(line.strip())  # Debug
        match = re.search(r'(https://[a-zA-Z0-9.-]+\.lhr\.life)', line)
        if match:
            url = match.group(1)
            break

    return url, process

# 2. Inicia o túnel
url, process = start_localhost_run(port=5000)

# 3. Mostra a URL pública
if url:
    print(f"\n🚀 Aplicação disponível em: {url}")
else:
    print("⚠️ Não foi possível obter a URL pública.")
