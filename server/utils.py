from flask import jsonify, request
import json 

def load_data():
    with open('data/database.json', 'r') as file:
        data = json.load(file)
    return data

def check_username(request):
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

