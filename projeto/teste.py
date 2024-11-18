from mysql.connector import (connection)

# cnx = connection.MySQLConnection(
#         host = '127.0.0.1',
#         user = 'root',  
#         password = 'labinfo', 
#         database = 'petShop'
#     )

# cursor = cnx.cursor(dictionary=True)

# sql = "SELECT * FROM animal"

# cursor.execute(sql)

# animais = cursor.fetchall()

# for animal in animais:
#     print(animal)

# cursor.close()
# cnx.close()

cnx = connection.MySQLConnection(
        host = '127.0.0.1',
        user = 'root',  
        password = 'labinfo', 
        database = 'pabd'
    )

cursor = cnx.cursor(dictionary=True)

sql = "SELECT * FROM info3m"

cursor.execute(sql)

alunos = cursor.fetchall()

for aluno in alunos:
    print(f"id: {aluno['id']}, nome: {aluno['nome']}, endereço: {aluno['endereco']}")

cursor.close()
cnx.close()

