import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')

banco = conexao.cursor()

infor = "select * from <nome da tabela>"

banco.execute(infor)

result = banco.fetchall()

for x in result:
    print(x)