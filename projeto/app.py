from flask import Flask, render_template, request
from mysql.connector import (connection)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/del')
def let():
    return render_template("del.html")

@app.route('/insert', methods = ['POST'])
def insert():
    nome = request.form['nome']
    raca = request.form['raca']

    cnx = connection.MySQLConnection(
        host = '127.0.0.1',
        user = 'root',  
        password = 'labinfo', 
        database = 'petShop'
    )

    sql = "INSERT INTO animal (nome, raca) VALUES (%s, %s)"
    tuple = (nome, raca)

    cursor = cnx.cursor()
    cursor.execute(sql, tuple)
    cnx.commit()

    cnx.close()

    return "deu certooooooooooooooooooooooooooo"

@app.route('/delete', methods = ['POST'])
def delete():
    id = request.form['id']

    cnx = connection.MySQLConnection(
        host = '127.0.0.1',
        user = 'root',  
        password = 'labinfo', 
        database = 'petShop'
    )

    sql = "DELETE FROM animal WHERE id = %s "
    tuple = (id,)

    cursor = cnx.cursor()
    cursor.execute(sql, tuple)
    cnx.commit()

    cnx.close()

    return "que Deus o tenha"
