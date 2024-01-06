
class WebUtils:
    @staticmethod
    def query_executor_wrapper(conn, query, values = None):
        if values:
            return conn.execute(query, values)
        else:
            return conn.execute(query)