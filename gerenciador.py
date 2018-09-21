
from flask import Flask, jsonify

app = Flask('Gerenciador')

tarefas = ['Rafael Messias'

'1,2,3,4']


@app.route('/tarefas')
def listar():
    return jsonify(tarefas)