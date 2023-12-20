import mysql.connector

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",     # Or your MySQL server's address
        user="root",          # MySQL username
        password="pass"   # MySQL password
    )
    print("Connected to MySQL successfully!")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # SQL command to create a database
    create_db_query = "CREATE DATABASE dcrm_app;"

    # Execute the SQL command
    cursor.execute(create_db_query)
    print("Database 'dcrm_app' created successfully!")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
