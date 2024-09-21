import pymysql


connection = pymysql.connect(
    host='localhost',         # Servidor MySQL, puede ser localhost o una IP
    user='root',        # Usuario de la base de datos MySQL
    password='Karm4Kill05.', # Contraseña del usuario MySQL
    database='sp500' # Nombre de la base de datos a la que te quieres conectar
)

cursor = connection.cursor()

cursor.execute(
)