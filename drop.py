from gbd import GBD
import MySQLdb

servidor = '127.0.0.1'
usuario = 'root'
senha = 'root'
bd = 'html'
con = MySQLdb.connect(servidor, usuario, senha)
cursor = con.cursor()
confirm = False
try:
    cursor.execute('drop schema {}'.format('bd'))
    print("Done")
except:
    print("BD doesn't exist")
