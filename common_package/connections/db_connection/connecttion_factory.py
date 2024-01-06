from common_package.connections.db_connection import mysql_db_connection

class ConnectionFactory:
    @staticmethod
    def create():
        conn = mysql_db_connection.MySqlDbConnection()
        conn.open()
        return  conn

