from gerenciador import app, tarefas

def test_listar_tarefas_deve_retornar_status_200():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        resposta = cliente.get('/tarefas')
        assert resposta.status_code == 200

def test_listar_tarefas_deve_ter_formato_json():
    with app.test_client() as cliente:
        resposta = cliente.get('/tarefas')
        assert resposta.content_type == 'application/json'

def test_lista_de_tarefas_vazia_retorna_lista_vazia():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        resposta = cliente.get('/tarefas')
        assert resposta.json == []

def test_lista_de_tarefas_nao_vazia_retorna_conteudo():
    tarefas.append({'id': 1, 'titulo': 'tarefa 1',
                    'descricao': 'tarefa de numero 1', 'estado': False})
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        resposta = cliente.get('/tarefas')
        assert resposta.json == [{
            'id': 1,
            'titulo': 'tarefa 1',
            'descricao': 'tarefa de numero 1',
            'estado': False}]
    tarefas.clear()


    