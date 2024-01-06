import traceback

from flask import request

class BaseHandler():
    def get_request(self, key):
        if request.method == 'POST':
            value = request.form.get(key, None)
            if value is None:
                data = request.get_json()
                value = data.get('body').get(key)
        else:
            value = request.args.get(key, None)

        if value is not None and (isinstance(value, str) or isinstance(value, bytes)):
            value = value
        return value

    def get_log_message(self, message):
        tb = traceback.format_exc()
        exceptopn_message = str(tb) if tb else ''
        return message + exceptopn_message
