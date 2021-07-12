# Python_Mysql (Guilherme Xavier Souza)

## Clonar Repostório
```
git clone https://github.com/Guilherme-full/Python_Mysql.git
```

|          | Linux | macOS | Windows |
|   :---   | :---: | :---: | :---:   |
| Chromium <!-- GEN:chromium-version -->93.0.4543.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| WebKit <!-- GEN:webkit-version -->14.2<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Firefox <!-- GEN:firefox-version -->89.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |

## Descrição
Material básico criado, para iniciantes que desejam trabalhar com banco de dados (mysql), utilizando a linguagem Python.

## Biblioteca
```
import mysql.connector
```

## Download Biblioteca (Pip)

```
pip install mysql.connector
ou
pip3 install mysql.connector
```

## Conexão com o banco de dados

```
import mysql.connector

try:
    conexao = mysql.connector.connect( host='<nome do host>', user= '<nome do usuario>', password= '<senha do usuario>')
except:
    print('Não foi possível realizar a conexão')
else:
    print('Conexão realizada com sucesso !')
```

## Criação de um Database

```
import mysql.connector

try:
    conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')
    banco = conexao.cursor()
    banco.execute('create database <nome do banco de dados>')
except:
    print('Erro na criação do banco de dados')
else:
    print('Banco de dados Criado com Sucesso')
```

## Consulta de tabela
```
import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')

banco = conexao.cursor()

infor = "select * from <nome da tabela>"

banco.execute(infor)

result = banco.fetchall()

for x in result:
    print(x)
```

## Criação de Tabela
```
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
 
```

## Inserção de dados em tabela
```
import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')
mybanco = conexao.cursor()

sql = "INSERT INTO <nome da tabela> (<nome da colunas>) VALUES (%s, %s, %s)"
val = [
  ('< Informações a serem inseridas >'),
  ('< Informações a serem inseridas >'),
  ('< Informações a serem inseridas >'),
  ('< Informações a serem inseridas >'),
  ('< Informações a serem inseridas >'),
]

mybanco.executemany(sql, val)

conexao.commit()

print(mybanco.rowcount, "was inserted.")
```

## Verificar Banco de Dados Existentes
```
import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')
banco = conexao.cursor()
banco.execute('show databases')
```

## Verificar Colunas
```
import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do usuario>', password='<senha do usuario>', database='<nome do banco de dados>')

banco = conexao.cursor()

banco.execute('select <nome das colunas> from <nome da tabela>')

x = banco.fetchall()

for i in x:
    print(i)
```

## Verificar Tabelas Existentes
```
  
import mysql.connector

conexao = mysql.connector.connect(host='<nome do host>', user='<nome do root>', password='<senha do usuario>', database='<nome do banco de dados>')
banco = conexao.cursor()
banco.execute('Show tables')
for x in banco:
    print(x)
```

## Ferramenta e Linguagem
<img align="center"  alt="Python" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></img>
<img align="center"  alt="Pycharm" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg"></img>
