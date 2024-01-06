from common_package.connections.db_connection import  connecttion_factory


class BaseHelper:
    def get_connection(self, existing_conn=None):
        conn = None
        try:
            if existing_conn is None:
                myconn = connecttion_factory.ConnectionFactory.create()
                conn = myconn.get_connection()
            else:
                conn = existing_conn
            return conn
        except:
            raise