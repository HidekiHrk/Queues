#!python3
from sys import argv as args

code_list = ['bank', 'estacionamento', 'hospital', 'eventos']

if len(args) > 1:
    if args[1] not in code_list:
        print(f"Código inválido. Valores possíveis: {', '.join(code_list)}")
    else:
        __import__(args[1]).main()
else:
    print(f"Digite o programa que deseja rodar.\n\tEx: {args[0]} [{'|'.join(code_list)}]")

