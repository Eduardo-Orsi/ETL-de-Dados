import mysql.connector as mysql
from mysql.connector import MySQLConnection


class DatabaseConnector:

    connection = None

    @classmethod
    def connect(cls) -> MySQLConnection:
        db_connection = mysql.connect(
            host="localhost",
            port=3306,
            database="pipeline_db",
            user="root",
            passwd="root"
        )
        cls.connection = db_connection
