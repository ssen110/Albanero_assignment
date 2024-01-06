from sqlalchemy import exc, text
from common_package.web_utils import  web_utils
from common_package.vo import seat_info_vo
from common_web_api.queries import seat_reservation_queries


class SeatReservationDao:

    def get_train_seat_booking(self, train_id, conn):
        try:
            query = text(seat_reservation_queries.SeatReservationQueries.get_train_seat_booking)
            values = {
                "train_id":train_id
            }
            result = web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            count = 0
            for row in result:
                count = row[0]
            return count
        except exc.SQLAlchemyError:
            raise


    def upgrade_train_ticket(self,train_id, conn):
        try:
            query = text(seat_reservation_queries.SeatReservationQueries.upgrade_train_ticket)
            values = {
                "train_id": train_id,
            }
            web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            conn.commit()
        except exc.SQLAlchemyError:
            raise

    def save_train_ticket_seat(self, user_id, train_id, is_confirmed,  conn):
        try:
            query = text(seat_reservation_queries.SeatReservationQueries.insert_into_seat_details)
            values = {
                "user_id": user_id,
                "train_id": train_id,
                "is_confirmed": is_confirmed,
            }
            web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            conn.commit()
        except exc.SQLAlchemyError:
            raise

    def cancel_train_ticket(self, booking_id, conn):
        try:
            query = text(seat_reservation_queries.SeatReservationQueries.cancel_train_ticket)
            values = {
                "booking_id": booking_id
            }
            web_utils.WebUtils.query_executor_wrapper(conn, query, values)
            conn.commit()
        except exc.SQLAlchemyError:
            raise