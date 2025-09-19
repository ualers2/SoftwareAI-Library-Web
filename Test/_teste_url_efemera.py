from flask import Flask
import threading
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def hello():
    return '🚀 Aplicação Flask exposta com sucesso via Localhost.run!'


app.run(host='0.0.0.0', port=5000)
