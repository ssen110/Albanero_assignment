
class SeatDetailsHandler:

    def save_train_ticket_seat(self):
        data = dict()
        message = None
        try:
            train_name = self.get_request("train_name")
            train_helper.TrainHelper().save_train_details(train_name, starting_place, ending_place, max_capacity, depurture_time, reaching_time)
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: save_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())