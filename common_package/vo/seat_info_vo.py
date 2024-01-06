class SeatInfoVo:
    def __int__(self):
        self._id = None
        self._user_id = None
        self._train_id = None
        self._is_confirmed = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def train_id(self):
        return self._train_id

    @train_id.setter
    def train_id(self, value):
        self._train_id = value

    @property
    def is_confirmed(self):
        return self._is_confirmed

    @is_confirmed.setter
    def is_confirmed(self, value):
        self._is_confirmed = value

    def serialize(self):
        d = dict()
        d['id'] = self._id
        d['train_id'] = self._train_id
        d['user_id'] = self._user_id
        d['is_confirmed'] = self._is_confirmed

        return  d

