from sqlalchemy import exc, text
from common_web_api.queries import train_queries
from common_package.web_utils import  web_utils
from common_package.vo import train_details_vo


class TrainDao:
    def get_train_details(self, train_id, conn):
        try:
            query = text(train_queries.TrainQueries.get_train_details)
            values = {
                "train_id":train_id
            }
            result = web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            train_detail = None
            for row in result:
                train_detail = train_details_vo.TrainDetailsVo()
                train_detail.id = row[0]
                train_detail.train_name = row[1]
                train_detail.source_station = row[2]
                train_detail.destination_station = row[3]
                train_detail.starting_time = row[4]
                train_detail.reaching_time = row[5]
                train_detail.max_capacity = row[6]
            return train_detail
        except exc.SQLAlchemyError:
            raise

    def save_train_details(self, train_name, starting_place, ending_place, max_capacity, depurture_time, reaching_time, conn):
        try:
            query = text(train_queries.TrainQueries.insert_into_user_details)
            values = {
                "train_name": train_name,
                "starting_place": starting_place,
                "ending_place": ending_place,
                "max_capacity": max_capacity,
                "depurture_time":depurture_time,
                "reaching_time":reaching_time
            }
            web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            conn.commit()
        except exc.SQLAlchemyError:
            raise