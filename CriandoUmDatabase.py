import mysql.connector

try:
    conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')
    banco = conexao.cursor()
    banco.execute('create database <nome do banco de dados>')
except:
    print('Erro na criação do banco de dados')
else:
    print('Banco de dados Criado com Sucesso')
