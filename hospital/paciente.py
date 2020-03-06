class Paciente:
    def __init__(self, nome, telefone, prioridade=0):
        self.nome = nome
        self.telefone = telefone
        self.prioridade = prioridade

    def __repr__(self):
        priorities = ['Sem urgência', 'Pouco urgente', 'Médio', 'Urgente', 'Muito urgente']
        return f"[Paciente: {self.nome} Tel: {self.telefone} Prioridade: {priorities[self.prioridade]}"