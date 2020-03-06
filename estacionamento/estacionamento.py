from queues import Queue

class Estacionamento(Queue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def removeCar(self, placa):
        removed = self.remove(placa)
        if removed:
            for car in removed:
                self.add(car)
            return True
        return False

    @property
    def carCount(self):
        return len(self)

    def getCars(self):
        return ' | '.join(map(lambda car: f"[carro: {car}]", self.values))