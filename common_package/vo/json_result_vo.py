class JsonresultVo:

    def __init__(self, value, message):
        self._data = value
        self._message = message

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def serialize(self):
        return {
            'data': self._data,
            'message': self._message
        }
