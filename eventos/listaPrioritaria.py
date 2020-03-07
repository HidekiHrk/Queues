from queues import Queue
from eventos.config import *

class ListaPrioritaria:
    def __init__(self):
        self.__prioridades = [[Queue() for _ in range(3)] for _ in range(3)]

    def registrarEvento(self, evento):
        ps = [evento.prioridade, evento.tipoPrioridade]
        p1, p2 = ps[::-1] if groupPriority else ps
        self.__prioridades[p1][p2].add(evento)

    def processarEventos(self):
        prioridades = self.__prioridades[::-1]
        for plist in prioridades:
            for prioridade in plist[::-1]:
                if len(prioridade) == 0: continue
                return prioridade.next()

    def processar(self):
        item = self.processarEventos()
        while item:
            yield item
            item = self.processarEventos()