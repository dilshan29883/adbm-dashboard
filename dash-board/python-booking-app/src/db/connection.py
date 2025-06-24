from mysql.connector import connect, Error

def get_db_connection():
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="",
            database="movie_theater"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None