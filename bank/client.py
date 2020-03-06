from bank.time import Time

class Client:
    def __init__(self):
        self.attended = None
        self.entered = Time().now
