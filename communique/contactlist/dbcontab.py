import psycopg2

# Funkcja do łączenia się z bazą danych PostgreSQL

def connect_to_postgresql():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Minecraft@2001",
            host="localhost",
            port="",                
            database="testbaza"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Błąd podczas łączenia się z bazą danych PostgreSQL:", error)

    # Funkcja do tworzenia tabeli
def create_table(connection, table_name):
    try:
        cursor = connection.cursor()
        create_table_query = f"""
            CREATE TABLE {table_name} (
                id SERIAL PRIMARY KEY,
                column1 VARCHAR(255),
                column2 INTEGER
            )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabela została utworzona pomyślnie!")
    except (Exception, psycopg2.Error) as error:
        print("Błąd podczas tworzenia tabeli:", error)

def get_table_names(connection):
    cursor = connection.cursor()
    query = """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_name LIKE 'contactlist\_%'
        """
    cursor.execute(query)

    tables_names = cursor.fetchall()

    cursor.close()
    connection.close()
    return tables_names
  
