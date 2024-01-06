from common_web_api import base_helper
class UserHelper(base_helper.BaseHelper):

    def get_user_details(self, user_id, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            print("my id : " + str(user_id))
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()