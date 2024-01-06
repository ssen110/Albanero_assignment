from common_web_api.helpers import base_helper
from common_web_api.dao import user_dao


class UserHelper(base_helper.BaseHelper):

    def get_user_details(self, user_id, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            return user_dao.UserDao().get_user_details(user_id, conn)
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def save_user_details(self, email_id, name, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            user_dao.UserDao().save_user_details(email_id, name, conn)
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()