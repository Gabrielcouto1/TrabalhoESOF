from flask import Flask, request, render_template
import os

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'TrabalhoESOF')
template_dir = os.path.join(template_dir, 'server')
template_dir = os.path.join(template_dir, 'static')
template_dir = os.path.join(template_dir, 'templates')

app = Flask("_name_", template_folder=template_dir)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/novoProduto")
def novoProduto():
    return render_template("novoProduto.html")

@app.route("/scrumBoard")
def scrumBoard():
    return render_template("scrumBoard.html")

@app.route("/scrum")
def scrum():
    return render_template("scrum.html")

@app.route("/xp")
def xp():
    return render_template("xp.html")


# pra adicionar uma nova rota
# @app.route("/NOME DA ROTA")
# def NOME DA FUNCAO():
#     return render_template("NOME DO ARQUIVO.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)