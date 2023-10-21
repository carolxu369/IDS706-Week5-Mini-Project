import mysql.connector
from mysql.connector import Error

def create_connection():
    # connect
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="interact"
        )
        print("Successfully connected to the database!")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def create_users_table(connection):
    # Creates the users table if not exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    );
    """
    execute_query(connection, create_table_query)

def close_connection(connection):
    # close
    if connection.is_connected():
        connection.close()
        print("Connection closed.")

def execute_query(connection, query):
    # execute
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully!")
    except Error as e:
        print(f"Error: '{e}'")

def get_all_data(connection, table_name):
    # read
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    return cursor.fetchall()

def main():
    # connection
    connection = create_connection()

    create_users_table(connection)

    # 1. CREATE operation: Add a new record
    create_query1 = """
    INSERT INTO users (name, age)
    VALUES ('John Doe', 25);
    """
    create_query2 = """
    INSERT INTO users (name, age)
    VALUES ('Milker', 10);
    """
    create_query3 = """
    INSERT INTO users (name, age)
    VALUES ('Alice', 20);
    """
    execute_query(connection, create_query1)
    execute_query(connection, create_query2)
    execute_query(connection, create_query3)

    # 2. READ operation: Fetch all data from users table
    all_data = get_all_data(connection, "users")
    print("Data in users table:", all_data)

    # 3. UPDATE operation: Update age for John Doe
    update_query = """
    UPDATE users
    SET age = 26
    WHERE name = 'John Doe';
    """
    execute_query(connection, update_query)

    # 4. DELETE operation: Remove a record with a specific name
    delete_query = """
    DELETE FROM users WHERE name = 'Milker';
    """
    execute_query(connection, delete_query)

    # Close the connection
    close_connection(connection)

if __name__ == "__main__":
    main()
