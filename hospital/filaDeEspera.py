from queues import Queue

class FilaDeEspera:
    def __init__(self, *args, **kwargs):
        self.__prioridades = [Queue() for _ in range(5)]

    def adicionarPaciente(self, paciente):
        self.__prioridades[paciente.prioridade].add(paciente)

    def operar(self):
        prioridades = self.__prioridades[::-1]
        for prioridade in prioridades:
            if len(prioridade) == 0: continue
            return prioridade.next()
        return "Nenhum paciente a ser operado."

    def __len__(self):
        return sum(map(lambda queue: len(queue), self.__prioridades))