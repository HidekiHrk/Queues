from hospital.filaDeEspera import FilaDeEspera
from hospital.paciente import Paciente

def choose(options):
    chosen = input(f"O que você deseja fazer? [{'|'.join(options)}]: ").lower().strip()
    while chosen not in options:
        print("Valor inválido, tente novamente!")
        chosen = input(f"O que você deseja fazer? [{'|'.join(options)}]: ").lower().strip()
    return chosen

def cadastrar():
    pass

def main():
    fde = FilaDeEspera()
    while True:
        choice_dict = {
            "cadastrar": cadastrar
        }
        chosen = choose(choice_dict.keys())
        choice_dict.get(chosen)()
