from flask import jsonify

from common_package.vo import json_result_vo
from common_web_api.helpers import seat_reserve_helper
from webapp.web_handlers import base_handler


class SeatDetailsHandler(base_handler.BaseHandler):

    def get_train_ticket_count_details(self):
        data = dict()
        message = None
        try:
            train_id = self.get_request("train_id")
            ticket_confirmed_count, remaining_ticket_count = seat_reserve_helper.SeatReserveHelper().get_train_seat_booking_details(train_id)
            data["confirmed_count"]  = ticket_confirmed_count
            data["vacant_count"] = remaining_ticket_count
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: save_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())


    def save_train_ticket_seat(self):
        data = dict()
        message = None
        try:
            user_id =  self.get_request("user_id")
            train_id =  self.get_request("train_id")
            seat_reserve_helper.SeatReserveHelper().save_train_ticket_seat(user_id, train_id)
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: save_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())

    def cancel_train_ticket(self):
        data = dict()
        message = None
        try:
            user_id = self.get_request("user_id")
            train_id = self.get_request("train_id")
            booking_id = self.get_request("booking_id")
            seat_reserve_helper.SeatReserveHelper().cancel_train_ticket(booking_id, user_id, train_id)
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: save_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())