from eventos.eventos import Grafico, Logico, Entrada
from eventos.listaPrioritaria import ListaPrioritaria
from random import randint, choice

def randomEvent():
    events = [Grafico, Logico, Entrada]
    event = choice(events)(randint(0,2))
    return event

def generateEvents(eventRange=[1,20]):
    for _ in range(randint(*eventRange)):
        yield randomEvent()

def getTimeInt():
    time_limit = None
    while True:
        try:
            time_limit = int(input("Tempo da simulação: "))
        except:
            print("Valor inválido, tente novamente.")
            continue
        if time_limit > 0: break
        print("Valor inválido, tente novamente.")
    return time_limit

def main():
    lista = ListaPrioritaria()
    tempo = getTimeInt()
    for t in range(tempo):
        print(f"Tempo {t}:")
        for event in generateEvents():
            print("Adicionando evento:", event.nome)
            lista.registrarEvento(event)
    print("-"*5, "Processando eventos:", "-"*5)
    for event in lista.processar():
        print("Processando evento:", event.nome)

