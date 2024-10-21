from flask import Flask

app = Flask(__name__)

@app.route('/<nome>')
def home(nome):
    return f"<h1>Hello, {nome}!</h1>"