import mariadb
import sys

def verbinde_datenbank():
    try:
        conn = mariadb.connect(
            user="Raphi",
            password="RaphiH",
            host="localhost",
            port=3306,
            database="schlumpfshop3"
        )
        return conn
    except mariadb.Error as e:
        print(f"Fehler bei der Verbindung: {e}")
        sys.exit(1)

def anrede_hinzufuegen(conn, neue_anrede):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO anrede (Anrede) VALUES (?)", (neue_anrede,))
    conn.commit()
