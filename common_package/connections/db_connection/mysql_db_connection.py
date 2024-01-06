from sqlalchemy import create_engine, exc
from common_package.const.local import  config

class MySqlDbConnection:
    def __init__(self):
        self.conn = None
        self.engine = None
        mysql_url = config.MYSQL_DATABASE_URI

        if not self.engine:
            self.engine = create_engine(mysql_url, pool_recycle=3600, pool_size=50)


    def getconnection(self):
        try:
            if self.conn is None or self.conn.closed:
                raise exc.SQLAlchemyError("Connection is already closed.")
            return self.conn
        except exc.SQLAlchemyError:
            raise

    def open(self):
        try:
            if self.conn is not None and not self.conn.closed:
                return
            self.conn = self.engine.connect()
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def close(self):
        try:
            if self.conn is not None and not self.conn.closed:
                self.conn.close()
        except exc.SQLAlchemyError:
            raise
        except:
            raise

