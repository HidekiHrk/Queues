from queues import Queue
from bank.time import Time

class Caixa(Queue):
    def __init__(self):
        super().__init__(0)
        self.__registers = []

    def resolveClients(self, quantity=1):
        now = Time().now
        items = [{"client": client, "time": Time().now} for client in self]
        self.add(client)
        return item