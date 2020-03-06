from queues import Queue

class Caixa(Queue):
    __lastId = 0

    def __init__(self):
        super().__init__()
        Caixa.__lastId += 1
        self.id = Caixa.__lastId
        self.__registers = []

    def resolveClients(self, quantity=1):
        if len(self) < quantity:
            quantity = len(self)
        if quantity == 0: return []
        clients = [self.next().attend() for _ in range(quantity)]
        self.__registers += clients
        return clients

    @property
    def clients(self):
        return self.__registers

    def mediumTime(self):
        return sum(map(lambda client: client.waitTime, self.__registers)) / len(self.__registers)

    def __repr__(self):
        return f"[Caixa No {self.id} - fila: {len(self)} - atendidos: {len(self.clients)}]"