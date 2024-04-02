from flask import Flask, request, render_template, jsonify
import utils

app = Flask("_name_", template_folder=utils.template_dir)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        print(request)
        print(request.form)
        return jsonify({'message': 'Form data received successfully'}), 200
            
        

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/novoProduto", methods=['GET', 'POST'])
def novoProduto():
    if request.method == "GET":
        return render_template("novoProduto.html")
    elif request.method == "POST":
        utils.cadastraProduto(request)

@app.route("/scrumBoard")
def scrumBoard():
    return render_template("scrumBoard.html")

@app.route("/scrum")
def scrum():
    return render_template("scrum.html")

@app.route("/xp")
def xp():
    return render_template("xp.html")

@app.route("/novoRelatorio")
def novoRelatorio():
    return render_template("novoRelatorio.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)