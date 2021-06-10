import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do root>', password='<senha do usuario>', database='<nome do banco de dados>')
banco = conexao.cursor()
banco.execute('Show tables')
for x in banco:
    print(x)