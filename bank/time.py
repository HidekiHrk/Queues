class Time(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, start=0):
        if(self.__initialized): return
        self.__initialized = True
        self.__value = start
    
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