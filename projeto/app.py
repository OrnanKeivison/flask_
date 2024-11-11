from flask import Flask
from mysql.connector import (connection)

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/insert')
def insert():
    cnx = connection.MySQLConnection(
        host = '127.0.0.1',
        user = 'root',  
        password = 'labinfo', 
        database = 'petShop'
    )

    sql = "INSERT INTO animal (nome, raca) VALUES (%s, %s)"
    tuple = ('Mel', 'poodle')

    cursor = cnx.cursor()
    cursor.execute(sql, tuple)
    cnx.commit()

    cnx.close()

    return "deu certooooooooooooooooooooooooooo"

@app.route('/delete')
def delete():
    cnx = connection.MySQLConnection(
        host = '127.0.0.1',
        user = 'root',  
        password = 'labinfo', 
        database = 'petShop'
    )

    sql = "DELETE FROM animal WHERE id = %s "
    tuple = (7,)

    cursor = cnx.cursor()
    cursor.execute(sql, tuple)
    cnx.commit()

    cnx.close()

    return "que Deus o tenha"
