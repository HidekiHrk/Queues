from bank.time import Time

class Client:
    def __init__(self):
        self.attended = None
        self.entered = Time().now

    def attend(self):
        self.attended = Time().now
        return self

    @property
    def waitTime(self):
        return (self.attended if self.attended else Time().now) - self.entered