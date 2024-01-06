from sqlalchemy import create_engine, exc
from common_package.const.local import  config
from sqlalchemy.orm import Session

class MySqlDbConnection:
    def __init__(self):
        self.conn = None
        self.engine = None
        self.session = None
        mysql_url = config.MYSQL_DATABASE_URI

        if not self.engine:
            self.engine = create_engine(mysql_url, pool_recycle = 3600, pool_size = 50)

    def get_connection(self):
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
            self.session = Session(bind=self.conn)
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def commit(self):
        try:
            if self.session is not None:
                self.session.commit()
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def rollback(self):
        try:
            if self.session is not None:
                self.session.rollback()
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

