from common_web_api.helpers import base_helper
from common_web_api.dao import train_dao

class TrainHelper(base_helper.BaseHelper):
    def get_train_details(self, train_id, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            return train_dao.TrainDao().get_train_details(train_id, conn)
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def save_train_details(self, train_name, starting_place, ending_place, max_capacity, depurture_time, reaching_time, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            train_dao.TrainDao().save_train_details(train_name, starting_place, ending_place, max_capacity, depurture_time, reaching_time, conn)
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()