
from flask import Flask, jsonify

app = Flask('Gerenciador')

tarefas = ['Rafael']


@app.route('/tarefas')
def listar():
    return jsonify(tarefas)