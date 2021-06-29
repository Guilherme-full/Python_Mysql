import mysql.connector

try:
    conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<nome da senha>', database='<nome do database>')
    create_database = '''create table <nome da tabela> (
                        <nome da coluna> <tipo de dado> <primary key>
                        <nome da coluna> <tipo de dado>
                        <nome da coluna> <tipo de dado>
                        <nome da coluna> <tipo de dado>)'''


    con = conexao.cursor()
    con.execute(create_database)

except mysql.connector.Error as erro:
    print(f'Erro ao criar a tabela, {erro}')

else:
    print('Tabela criada com sucesso')
    con.close()
    conexao.close()

finally:
    print('Conexão finalizada')
    print('-' * 50)

