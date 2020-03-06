from hospital.filaDeEspera import FilaDeEspera
from hospital.paciente import Paciente

fila = FilaDeEspera()
numero_de_prioridades = 5

def choose(options):
    chosen = input(f"O que você deseja fazer? [{'|'.join(options)}]: ").lower().strip()
    while chosen not in options:
        print("Valor inválido, tente novamente!")
        chosen = input(f"O que você deseja fazer? [{'|'.join(options)}]: ").lower().strip()
    return chosen

def getPriorityValue(prange=[1,5]):
    priority = None
    while True:
        try:
            priority = int(input("Grau de urgência (1 a 5): "))
        except:
            print("Valor inválido, tente novamente.")
            continue
        if priority >= prange[0] and priority <= prange[1]: break
        print("Valor inválido, tente novamente.")
    return priority - 1

def cadastrar():
    nome = input("Nome do paciente: ")
    telefone = input("Telefone do paciente: ")
    prioridade = getPriorityValue([1, numero_de_prioridades])
    fila.adicionarPaciente(Paciente(nome, telefone, prioridade))

def operar():
    paciente = fila.operar()
    print("Paciente a ser operado:", paciente, sep='\n\t')

def main():
    while True:
        choice_dict = {
            "cadastrar": cadastrar,
            "operar": operar,
            "fila": lambda: print(f"Tamanho da fila: {len(fila)} pacientes."),
            "sair": exit
        }
        chosen = choose(choice_dict.keys())
        choice_dict.get(chosen)()

