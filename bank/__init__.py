from bank.time import Time
from bank.caixa import Caixa
from bank.client import Client
from bank.config import dynamic, client_quantity, client_resolve_limit
from random import randint

def addClients(caixas):
    if dynamic['activated']:
        quantity = randint(*dynamic["client_quantity_range"])
    else:
        quantity=client_quantity
    for i in range(quantity):
        caixa = min(caixas)
        caixa.add(Client())
    return caixas

def getMediumTime(caixas):
    return sum(map(lambda caixa: caixa.mediumTime(), caixas)) / len(caixas)

def getTimeInt():
    time_limit = None
    while True:
        try:
            time_limit = int(input("Limite de tempo (minutos): "))
        except:
            print("Valor inválido, tente novamente.")
            continue
        if time_limit > 0: break
        print("Valor inválido, tente novamente.")
    return time_limit

def main():
    caixa_list = [Caixa() for _ in range(5)]
    time = Time()
    time_limit = getTimeInt()
    for t in range(time_limit):
        print(f"Minuto {t}:")
        addClients(caixa_list)
        for caixa in caixa_list:
            client_resolve = randint(*dynamic['client_resolve_range']) if dynamic['activated'] else client_resolve_limit
            clients = caixa.resolveClients(quantity=client_resolve)
            print(
                f"Caixa No {caixa.id}:",
                f"Sendo atendidos: {len(clients)}",
                f"Na fila: {len(caixa)}", sep="\n\t"
            )
        time.fwd()
    for caixa in caixa_list:
        print(f"Média de tempo de espera na fila do caixa {caixa.id}: {caixa.mediumTime():.3f} minutos")
    print(f"Média de tempo de espera: {getMediumTime(caixa_list):.3f} minutos")