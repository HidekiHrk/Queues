class Time(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, start=0):
        self.__value = 0
    
    @property
    def now(self):
        return self.__value

    def set(self, value:float):
        self.__value = value

    def fwd(self):
        self.__value += 1

    def add(self, value:float):
        self.__value += value
        return self.__value

    def __add__(self, value):
        return self.add(value)