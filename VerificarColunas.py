import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')

banco = conexao.cursor()

banco.execute('select <nome das colunas> from <nome da tabela>')

x = banco.fetchall()

for i in x:
    print(i)