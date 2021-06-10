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


