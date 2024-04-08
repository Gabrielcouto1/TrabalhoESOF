from flask import Flask, request, render_template, jsonify # type: ignore
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
        return utils.fazLogin(request)
            
        

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/novoProduto", methods=['GET', 'POST'])
def novoProduto():
    if request.method == "GET":
        return render_template("novoProduto.html")
    elif request.method == "POST":
        return utils.cadastraProduto(request)

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

@app.route("/novoRelease", methods=['GET', 'POST'])
def novoRelease():
    if request.method == "GET":
        return render_template("novoRelease.html")
    elif request.method == "POST":
        return utils.cadastraRelease(request)

@app.route("/novoIteracao", methods=['GET', 'POST'])
def novoIteracao():
    if request.method == "GET":
        return render_template("novoIteracao.html")
    elif request.method == "POST":
        return utils.cadastraIteracao(request)

@app.route("/novoHistoria", methods=['GET', 'POST'])
def novoHistoria():
    if request.method == "GET":
        return render_template("novoHistoria.html")
    elif request.method == "POST":
        return utils.cadastraHistoria(request)


@app.route("/novoTarefa", methods=['GET', 'POST'])
def novoTarefa():
    if request.method == "GET":
        return render_template("novoTarefa.html")
    elif request.method == "POST":
        return utils.cadastraTarefa(request)

@app.route("/kanban")
def kanban():
    return render_template("kanban.html")

@app.route("/getProductNames")
def getProductNames():
    data = utils.load_data()
    product_names = [product['productName'] for product in data['scrumProducts']]
    
    return jsonify(product_names)

@app.route("/viewProduct")
def viewProduct():
    product_name = request.args.get('productName')
    data = utils.load_data()

    product = next((p for p in data['scrumProducts'] if p['productName'] == product_name), None)
    return render_template("view_product.html", product=product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)