from estacionamento.estacionamento import Estacionamento

def choose(options):
    chosen = input(f"O que você deseja fazer? [{'|'.join(options)}]: ").lower().strip()
    while chosen not in options:
        print("Valor inválido, tente novamente!")
        chosen = input(f"O que você deseja fazer? [{'|'.join(options)}]: ").lower().strip()
    return chosen

def main():
    estacionamento = Estacionamento()
    while True:
        choose_dict = {
            'add':lambda: estacionamento.add(input("Placa: ")),
            'rm':lambda: estacionamento.removeCar(input("Placa: ")),
            's':lambda: print("Carros:", estacionamento.getCars() if len(estacionamento) else "Estacionamento Vazio"),
            'sair':lambda: exit()
        }
        choice = choose(choose_dict.keys())
        choose_dict.get(choice)()