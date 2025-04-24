from funktionen import verbinde_datenbank, anrede_hinzufuegen

def main():
    conn = verbinde_datenbank()
    anrede = input("Gebe eine neue Anrede ein: ")
    anrede_hinzufuegen(conn, anrede)
    print("Anrede hinzugefügt.")

if __name__ == "__main__":
    main()
