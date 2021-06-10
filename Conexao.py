import mysql.connector

try:
    conexao = mysql.connector.connect( host='<nome do host>', user= '<nome do usuario>', password= '<senha do usuario>')
except:
    print('Não foi possível realizar a conexão')
else:
    print('Conexão realizada com sucesso !')


