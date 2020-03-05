from queues import Queue
from bank.time import Time

class Caixa(Queue):
    def __init__(self):
        super().__init__(0)
        
    def addClient(client):
        item = {"client":client, "time":Time().now}
        self.add(item)
        return item

    