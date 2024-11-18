from flask import Flask, render_template, request
from mysql.connector import (connection)

app = Flask(__name__)

@app.route('/ins')
def home():
    return render_template("form.html")

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

@app.route('/del')
def let():
    return render_template("del.html")

@app.route('/delete', methods = ['POST'])
def delete():
    id = request.form['id']

    cnx = connection.MySQLConnection(
        host = '127.0.0.1',
        user = 'root',  
        password = 'labinfo', 
        database = 'petShop'
    )
    sqlshow = "SELECT (nome, raca) FROM animal WHERE id = %s "

    sql = "DELETE FROM animal WHERE id = %s "

    tuple = (id,)

    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sqlshow, tuple)
    animal = cursor.fetchall()
    
    for animal in animal:
        msm = f"vc deseja realmente deletar o {animal['nome']}, que tem a raça: {animal['raca']}"

    cnx.commit()

    cnx.close()

    return msm

@app.route('/show')
def show():
    cnx = connection.MySQLConnection(
            host = '127.0.0.1',
            user = 'root',  
            password = 'labinfo', 
            database = 'petShop'
        )

    cursor = cnx.cursor(dictionary=True)

    sql = "SELECT * FROM animal"

    cursor.execute(sql)

    animais = cursor.fetchall()

    # for animal in animais:
    #     print(animal)
    
    cursor.close()
    cnx.close()

    return render_template("show.html", animais = animais)