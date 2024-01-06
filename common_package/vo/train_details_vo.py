class TrainDetailsVo:
    def __int__(self):
        self._id = None
        self._train_name = None
        self._source_station = None
        self._destination_station = None
        self._starting_time = None
        self._reaching_time = None
        self._max_capacity = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def train_name(self):
        return self._train_name

    @train_name.setter
    def train_name(self, value):
        self._train_name = value

    @property
    def source_station(self):
        return self._source_station

    @source_station.setter
    def source_station(self, value):
        self._source_station = value

    @property
    def destination_station(self):
        return self._destination_station

    @destination_station.setter
    def destination_station(self, value):
        self._destination_station = value

    @property
    def starting_time(self):
        return self._starting_time

    @starting_time.setter
    def starting_time(self, value):
        self._starting_time = value

    @property
    def reaching_time(self):
        return self._reaching_time

    @reaching_time.setter
    def reaching_time(self, value):
        self._reaching_time = value

    @property
    def max_capacity(self):
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value):
        self._max_capacity = value

    def serialize(self):
        d = dict()
        d['id'] = self._id
        d['train_name'] = self._train_name
        d['source_station'] = self._source_station
        d['destination_station'] = self._destination_station
        d['starting_time'] = self._starting_time
        d['reaching_time'] = self._reaching_time
        d['max_capacity'] = self._max_capacity

        return d
