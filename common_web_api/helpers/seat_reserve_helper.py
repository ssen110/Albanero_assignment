from common_web_api.dao import seat_reservation_dao
from common_web_api.helpers import base_helper, train_helper

class SeatReserveHelper(base_helper.BaseHelper):

    def get_train_seat_booking(self, train_id,  existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            return seat_reservation_dao.SeatReservationDao().get_train_seat_booking(train_id, conn)
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def get_train_seat_booking_details(self, train_id, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            ticket_confirmed_count = seat_reservation_dao.SeatReservationDao().get_train_seat_booking(train_id, conn)
            train_details = train_helper.TrainHelper().get_train_details(train_id)
            remaining_ticket_count = train_details.max_capacity - ticket_confirmed_count
            return ticket_confirmed_count, remaining_ticket_count
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()


    def save_train_ticket_seat(self, user_id, train_id, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            train_details = train_helper.TrainHelper().get_train_details(train_id)
            already_confirmed_train_ticket_count = self.get_train_seat_booking(train_id, conn)
            is_confirmed = 0
            if train_details.max_capacity  < already_confirmed_train_ticket_count:
                is_confirmed = 1
            seat_reservation_dao.SeatReservationDao().save_train_ticket_seat(user_id, train_id, is_confirmed, conn)

            return "Success" if is_confirmed else "In Queue"
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def cancel_train_ticket(self, booking_id, user_id, train_id, existing_conn = None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            seat_reservation_dao.SeatReservationDao().cancel_train_ticket(booking_id, conn)
            seat_reservation_dao.SeatReservationDao().upgrade_train_ticket(train_id, conn)
        except Exception as e:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()