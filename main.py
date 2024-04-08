from classes.Carros import *
from classes.Clientes import *
from classes.Locacoes import *
import os

opcao: int = None

menu_inicial: str = '''[1] Locações
[2] Clientes
[3] Carros
[9] Sair'''

menu_locacoes: str = '''[1] Nova locação
[2] Finalizar Locação
[3] Relatório de carros locados
[8] Voltar ao menu inicial
[9] Sair'''

menu_clientes: str = '''[1] Cadastrar novo
[2] Atualizar informações
[3] Localizar locações
[8] Voltar ao menu inicial
[9] Sair'''

menu_carros: str = '''[1] Cadastrar novo
[2] Atualizar informações
[3] Excluir um carro
[4] Disponibilizar carros para venda
[5] Localizar carros por categoria
[8] Voltar ao menu inicial
[9] Sair'''

print(menu_inicial)



while opcao != 9:


    opcao = int(input("Digite o número da opção desejada: "))


    match opcao:
        case 1:
            os.system('cls')
            print(menu_locacoes)
        case 2:
            os.system('cls')
            print(menu_clientes)
        case 3:
            os.system('cls')
            print(menu_carros)
        case 8:
            os.system('cls')
            print(menu_inicial)

print("Sessão finalizada! Volte sempre!")

