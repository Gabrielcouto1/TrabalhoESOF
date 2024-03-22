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
    return render_template("landing_page.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)