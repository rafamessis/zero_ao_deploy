
from flask import Flask, jsonify

app = Flask('Gerenciador')

tarefas = []


@app.route('/tarefas')
def listar():
    return jsonify(tarefas)