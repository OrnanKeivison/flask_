from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<nome>')
def home(nome):
    return render_template('home.html', nome = nome)

@app.route('/login')
def login():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    nome = request.form['nome']
    senha = request.form['senha']

    if senha == '123456':
        mensagem = f'parabéns vc está logado {nome}!'

    else:
        mensagem = 'se logue direito rapais'

    return render_template('answer.html', mensagem = mensagem)
    
