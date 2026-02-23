import mysql.connector

def connect_db():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysqlhk@123",
            database="student_db"
        )
        if connection.is_connected():
            print("connected to mysql database")
            return connection
    except mysql.connector.Error as err:
        print("Error connecting to mysql: ",err)
        return None