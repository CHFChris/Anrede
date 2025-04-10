import mariadb
import sys

try:
    conn = mariadb.connect(
        user="Raphi",
        password="RaphiH",
        host="localhost",
        port=3306,
        database="schlumpfshop3"
    )
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
 
 
abfrage = conn.cursor()
anrede = input("Gebe eine neue Anrede ein: ")
abfrage.execute(f"INSERT INTO anrede(anrede.Anrede) VALUES(\"{anrede}\");")
conn.commit()