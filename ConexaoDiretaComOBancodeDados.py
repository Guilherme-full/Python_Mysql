import mysql.connector
try:
    conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')
except:
    print('Conexão não realizada !')
else:
    print('Conexão realizada com sucesso !')