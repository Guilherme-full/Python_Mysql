import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')

banco = conexao.cursor()

banco.execute('select * from <nome da tabela>')

result = banco.fetchone()

print(result)