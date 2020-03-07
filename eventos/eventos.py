class Evento:
    priority_names = ['Baixa', 'Média', 'Alta']
    prioridade = 0
    def __init__(self, prioridade=0):
        self.prioridade = prioridade

    @property
    def nome(self):
        return self.__class__.priority_names[self.prioridade]

    @property
    def tipoPrioridade(self):
        return self.__class__.prioridade

    def __repr__(self):
        return f"[Evento: {self.nome} - Prioridade: {['Baixa', 'Média', 'Alta'][self.prioridade]} - Tipo: {self.__class__.__name__}]"

class Grafico(Evento):
    priority_names = ['Partículas', 'Atualização de Tela', 'Colisão']
    prioridade = 2

class Logico(Evento):
    priority_names = ['Simulação Física', 'Inteligência Artificial', 'Lógica do Jogo']
    prioridade = 1

class Entrada(Evento):
    priority_names = ['Internet', 'Mouse', 'Teclado']
    prioridade = 0
