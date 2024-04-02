from flask import jsonify
import os
import json 

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'TrabalhoESOF')
template_dir = os.path.join(template_dir, 'server')
template_dir = os.path.join(template_dir, 'static')
template_dir = os.path.join(template_dir, 'templates')

def load_data():
    with open('data/database.json', 'r', encoding='utf8') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open('data/database.json', 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4)

def format_form(raw_data):
    username_start = raw_data.find('username') + len('username') + 3
    username_end = raw_data.find('------', username_start) - 4
    username = raw_data[username_start:username_end]

    password_start = raw_data.find('password') + len('password') + 3
    password_end = raw_data.find('------', password_start) - 4
    password = raw_data[password_start:password_end]

    username = username.replace("\\n\\r\\n", "")
    password = password.replace("\\n\\r\\n", "")

    return [username,password]
     
def fazLogin(request):
    data = load_data()

    username, password = format_form(str(request.form))

    for user in data['users']:
        if user['username'] == username and user['password'] == password:
                return jsonify({'exists': True}), 200

    return jsonify({'exists': False}), 200

def cadastraProduto(request):
    data = load_data()

    newProduct ={
        "productName": request.form.get('nome_produto'),
        "scrumMaster": request.form.get('scrum_master'),
        "productOwner": request.form.get('dono_produto'),
        "sprintBacklog": request.form.get('backlog_sprint'),
        "devs": request.form.get('devs'),
        "beginDate": request.form.get('dataInicio'),
        "endDate": request.form.get('dataFim')
    }

    data['scrumProducts'].append(newProduct)
    save_data(data)

    return jsonify({'message': True}), 200

