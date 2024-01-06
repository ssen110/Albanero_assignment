from sqlalchemy import exc, text
from common_web_api.queries import  user_queries
from common_package.web_utils import  web_utils
from common_package.vo import user_vo


class UserDao:
    def get_user_details(self, user_id, conn):
        try:
            query = text(user_queries.UserQueries.get_user_details)
            values = {
                "user_id":user_id
            }
            result = web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            user_details = None
            for row in result:
                user_details = user_vo.UserVo()
                user_details.id = row[0]
                user_details.email_id = row[1]
                user_details.user_name = row[2]
            return user_details
        except exc.SQLAlchemyError:
            raise


    def save_user_details(self, email_id, name, conn):
        try:
            query = text(user_queries.UserQueries.insert_into_user_details)
            values = {
                "email_id" : email_id,
                "name": name
            }
            web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            conn.commit()
        except exc.SQLAlchemyError:
            conn.rollback()
            raise
