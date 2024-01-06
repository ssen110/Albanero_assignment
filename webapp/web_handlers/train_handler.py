from flask import jsonify
from webapp.web_handlers import base_handler
from common_package.vo import json_result_vo
from common_web_api.helpers import  train_helper

class TrainHandler(base_handler.BaseHandler):
    def get_train_details(self):
        data = dict()
        message = None
        try:
            train_id = self.get_request("train_id")
            result = train_helper.TrainHelper().get_train_details(int(train_id))
            data["data"] = result.serialize()
            message = "Success"
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: get_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())

    def save_train_details(self):
        data = dict()
        message = None
        try:
            train_name = self.get_request("train_name")
            starting_place = self.get_request("starting_place")
            ending_place = self.get_request("ending_place")
            max_capacity = self.get_request("max_capacity")
            depurture_time = self.get_request("depurture_time")
            reaching_time = self.get_request("reaching_time")
            train_helper.TrainHelper().save_train_details(train_name, starting_place, ending_place, max_capacity, depurture_time, reaching_time)
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: save_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())
