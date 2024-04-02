from flask import jsonify
import os
import json 

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'TrabalhoESOF')
template_dir = os.path.join(template_dir, 'server')
template_dir = os.path.join(template_dir, 'static')
template_dir = os.path.join(template_dir, 'templates')

def load_data():
    with open('data/database.json', 'r') as file:
        data = json.load(file)
    return data

def fazLogin(request):
    data = load_data()
    raw_data = str(request.form)

    username_start = raw_data.find('username') + len('username') + 3
    username_end = raw_data.find('------', username_start) - 4
    username = raw_data[username_start:username_end]

    password_start = raw_data.find('password') + len('password') + 3
    password_end = raw_data.find('------', password_start) - 4
    password = raw_data[password_start:password_end]

    username = username.replace("\\n\\r\\n", "")
    password = password.replace("\\n\\r\\n", "")

    for user in data['users']:
        if user['username'] == username and user['password'] == password:
                return jsonify({'exists': True}), 200

    return jsonify({'exists': False}), 200

def cadastraProduto(request):
    nome_produto = request.form.get('nome_produto')
    scrum_master = request.form.get('scrum_master')
    dono_produto = request.form.get('dono_produto')
    backlog_sprint = request.form.get('backlog_sprint')
    devs = request.form.get('devs')
    dataInicio = request.form.get('dataInicio')
    dataFim = request.form.get('dataFim')

    print('Nome do Produto:', nome_produto)
    print('Scrum Master:', scrum_master)
    print('Dono do Produto:', dono_produto)
    print('Backlog da Sprint:', backlog_sprint)
    print('Devs:', devs)
    print('Data de Início:', dataInicio)
    print('Data Final:', dataFim)

    return jsonify({'message': True}), 200