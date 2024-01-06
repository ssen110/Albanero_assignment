class UserVo:
    def __int__(self):
        self._id = None
        self._user_name = None
        self._email_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    @property
    def email_id(self):
        return self._email_id

    @email_id.setter
    def email_id(self, value):
        self._email_id = value

    def serialize(self):
        d = dict()
        d['id'] = self._id if self._id else None
        d['email_id'] = self._email_id if  self._email_id else None
        d['user_name'] = self._user_name if self._user_name else None

        return d