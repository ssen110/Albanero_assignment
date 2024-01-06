from flask import request, jsonify
from webapp.web_handlers import base_handler
from common_package.vo import json_result_vo
from common_web_api import user_helper

class UserHandler(base_handler.BaseHandler):
    def get_user_details(self):
        data = dict()
        message = None
        try:
            user_helper.UserHelper().get_user_details(1212)
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: get_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())
