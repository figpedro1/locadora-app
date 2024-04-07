from classes.Carros import *
from classes.Clientes import *
from classes.Locacoes import *
import os

class Tela:

    def __init__(self, caminho_locacoes, caminho_clientes, caminho_carros):

        self.clientes = Clientes(caminho_clientes)
        self.carros = Carros(caminho_carros)

    @staticmethod
    def limpar_tela():
        os.system('cls')


    def tela_inicial(self):

        while True:
            self.limpar_tela()

            print(
            '''
            [1] Locações
            [2] Clientes
            [3] Carros
            [9] Sair
            '''
            )

            opcao = int(input("Digite a opção desejada: "))

        
            match opcao:
                case 1:
                    self.tela_locacoes()
                case 2:
                    self.tela_clientes()
                case 3:
                    self.tela_carros()
                case 9:
                    return
        
    def tela_locacoes(self):

        while True: 
            self.limpar_tela()

            print(
            '''
            [1] Nova locação
            [2] Finalizar Locação
            [3] Relatório de carros locados
            [9] Sair
            '''
            )

            opcao = int(input("Digite a opção desejada"))

            match opcao:
                case 1:
                    print("Nova locação")
                case 2:
                    print("Finaliza locação")
                case 3:
                    print("Relatório de de carros")
                case 9:
                    return
    
    def tela_clientes(self):

        while True:
            self.limpar_tela()
            
            print(
            '''
            [1] Cadastrar novo
            [2] Atualizar informações
            [3] Localizar locações
            [9] Sair
            '''
            )

            opcao = int(input("Digite a opção desejada"))

            match opcao:
                case 1:
                    self.cadastrar_cliente()
                case 2:
                    self.atualizar_cliente()
                case 3:
                    print("Bruh")
                case 9:
                    return

    def tela_carros(self):

        while True:

            self.limpar_tela()

            print(
            '''
            [1] Cadastrar novo
            [2] Atualizar informações
            [3] Excluir um carro
            [4] Disponibilizar carros para venda
            [5] Localizar carros por categoria
            [9] Sair
            '''
            )

            opcao = int(input("Digite a opção desejada"))

            match opcao:
                case 1:
                    self.cadastrar_carro()
                case 2:
                    self.atualizar_carro()
                case 5:
                    self.localiza_carro()

    def nova_locacao():

        locacao = Locacao()





    
                
    def cadastrar_cliente(self):

        novo_cliente = Cliente(vazio = True)

        self.limpar_tela()
        while True:
            try:
                novo_cliente.set_cpf(input("Digite seu CPF: "))
                self.limpar_tela()
                break

            except ValueError:
                print("CPF inválido!")
        
        novo_cliente.set_nome(input("Digite seu nome completo: "))
        self.limpar_tela()

        while True:
            try:
                self.limpar_tela()
                novo_cliente.set_idade(input("Digite sua idade: "))
                self.limpar_tela()
                break
            
            except ValueError:
                print("Idade inválida!")

        novo_cliente.set_endereco(input("Digite seu endereço: "))
        self.limpar_tela()
        
        novo_cliente.set_cidade(input("Digite sua cidade: "))
        self.limpar_tela()

        novo_cliente.set_estado(input("Digite seu estado: "))
        self.limpar_tela()

        self.clientes.add_cliente(novo_cliente)
        print("Cliente cadastrado com sucesso!")
        input("Aprente [ENTER] para continuar")
        return

    def atualizar_cliente(self):

        self.limpar_tela()

        opcao: int = None

        while True:

            try:
                cpf = Cliente.formatar_cpf(input("Digite o CPF do cliente que deseja alterar: "))
                self.limpar_tela()  
                break
            
            except ValueError:
                print("CPF inválido!")

        try:
            cliente = self.clientes.get_cliente(cpf)

        except IndexError:
            print("Cliente não cadastrado!")
            input("Aprente [ENTER] para continuar")
            return
        
        self.limpar_tela()
        while True:

            print(
            '''
            [1] Nome
            [2] Idade
            [3] Endereço
            [4] Cidade
            [5] Estado
            [9] Salvar e sair
            '''      
            )

            opcao = int(input("Selecione o dado que deseja alterar: "))    
            self.limpar_tela()

            match opcao:

                case 1:
                    cliente.set_nome(input("Digite o novo nome"))
                    self.limpar_tela()
                case 2:
                    try:
                        cliente.set_idade(input("Digite a nova idade"))
                        self.limpar_tela()
                        
                    except ValueError:
                        print("Idade inválida!")

                case 3:
                    cliente.set_endereco(input("Digite o seu novo endereço"))
                    self.limpar_tela()
                case 4:
                    cliente.set_cidade(input("Digite a nova cidade"))
                    self.limpar_tela()
                case 5:
                    cliente.set_estado(input("Digite o novo estado"))
                    self.limpar_tela()
                case 9:
                    self.clientes.salvar_csv()
                    self.limpar_tela()
                    return

    def cadastrar_carro(self):

        novo_carro = Carro(vazio = True)

        self.limpar_tela()
        while True:
            try:
                novo_carro.set_modelo(input("Digite o modelo do seu carro: "))
                self.limpar_tela()
                break

            except ValueError:
                print("Modelo inválido!")
        
        while True:
            try:
                novo_carro.set_cor(input("Digite a cor do seu carro: "))
                self.limpar_tela()
                break

            except ValueError:
                print("Cor inválida")

        while True:
            try:
                novo_carro.set_ano(input("Digite o ano de lançamento do seu carro: "))
                self.limpar_tela()
                break
            
            except ValueError:
                print("Ano inválido!")

        while True:
            try:
                novo_carro.set_placa(input("Digite a placa do seu carro: "))
                self.limpar_tela()
                break
            
            except ValueError:
                print("Placa inválida!")
        
        while True:
            try:
                novo_carro.set_cambio(input("Digite o cambio do seu carro: "))
                self.limpar_tela()
                break
            except ValueError:
                print("Cambio inválido!")
        
        while True:
            try:
                novo_carro.set_categoria(input("Digite a categoria do seu carro: "))
                self.limpar_tela()
                break
            except ValueError:
                print("Categoria inválida!")

        while True:
            try:
                novo_carro.set_quilometragem(input("Digite a quilometragem do seu carro: "))
                self.limpar_tela()
                break
            except ValueError:
                print("Quilometragem inválida!")
        
        while True:
            try:
                novo_carro.set_diaria(input("Digite o valor do aluguel diário do seu carro: "))
                self.limpar_tela()
                break
            except ValueError:
                print("Valor inválido!")

        while True:
            try:
                novo_carro.set_seguro(input("Digite o custo do seguro do seu carro: "))
                self.limpar_tela()
                break
            except ValueError:
                print("Seguro inválido!")
            
        while True:
            try:
                novo_carro.set_disponivel(input("Tecle [1] se o seu carro estiver disponível ou [0] caso não esteja: "))
                self.limpar_tela()
                break
            except ValueError:
                print("Tecla inválida")


        self.carros.add_carro(novo_carro)
        print("Carro cadastrado com sucesso!")
        input("Aprente [ENTER] para continuar")
        return
    
    def atualizar_carro(self):

        self.limpar_tela()
        while True:
            

            carro = self.carros.get_carro(int(input("Digite o ID do carro que deseja alterar informações")))



            print(
            '''
            [1] Modelo
            [2] Cor
            [3] Ano
            [4] Placa
            [5] Cambio
            [6] Categoria
            [7] Quilometragem
            [8] Aluguel
            [9] Seguro
            [10] Disponibilidade
            [0] Salvar e sair
            '''      
            )

            opcao = int(input("Selecione o dado que deseja alterar: "))    
            self.limpar_tela()

            match opcao:

                case 1:
                    try:
                        carro.set_modelo(self, input("Digite a nova cor do seu carro"))
                        self.limpar_tela()
                    except ValueError:
                        print("Modelo inválido!")

                case 2:
                    try:
                        carro.set_cor(self, input("Digite a nova cor do seu carro"))
                        self.limpar_tela()
                        
                    except ValueError:
                        print("Cor inválida!")

                case 3:
                    try:
                        carro.set_ano(input("Digite o novo ano do seu carro"))
                        self.limpar_tela()
                    except ValueError:
                            print("Ano inválido!")
                        
                case 4:
                    try:
                        carro.set_placa(input("Digite a nova placa do seu carro"))
                        self.limpar_tela()
                    except ValueError:
                        print("Placa inválida!")

                case 5:
                    try:
                        carro.set_cambio(input("Digite o novo câmbio do seu carro"))
                        self.limpar_tela()
                    except ValueError:
                        print("Câmbio inválido")

                case 6:
                    try:
                        carro.set_quilometragem("Digite a nova quilometragem do seu carro")
                        self.limpar_tela()
                    except ValueError:
                        print("Quilometragem inválida!")
                    

                case 7:
                    try:
                        carro.set_diaria("Digite o novo valor de aluguel diário do seu carro")
                        self.limpar_tela()
                    except ValueError:
                        print("Valor inválido!")
                    

                case 8:
                    try:
                        carro.set_quilometragem("Digite a nova quilometragem do seu carro")
                        self.limpar_tela()
                    except ValueError:
                        print("Quilometragem inválida!")
                    

                case 9:
                    try:
                        carro.set_seguro("Digite o novo seguro do seu carro")
                        self.limpar_tela()
                    except ValueError:
                        print("Informação inválida!")
                    
                
                case 9:
                    try:
                        carro.set_quilometragem("Digite a nova quilometragem do seu carro")
                        self.limpar_tela()
                    except ValueError:
                        print("Quilometragem inválida!")
                    

                case 10:
                    try:
                        carro.set_disponivel("Tecle [1] para definir seu carro como disponível ou tecle [2] para indisponível")
                        self.limpar_tela()
                    except ValueError:
                        print("Tecla inválida!")
                    


    #                   FUNCIONALIDADE DE EXCLUSÃO DE CARROS                   


    #                   FUNCIONALIDADE DE DISPONIBILIZAÇÃO PARA VENDA


    def localiza_carro(self):

        self.limpar_tela()

        while(True):
            
            try:
                id = self.carros.get_id_categoria(input("Digite o câmbio do seu carro", input("Digite a categoria do seu carro")))
                break

            except ValueError:
                ("Câmbio ou categoria inválidos!")

        opcao = 0

        while(True):


            carro = self.carros.get_carro(id[opcao])

            print("Modelo: " + carro.get_modelo())
            print("Cor: " + carro.get_cor())
            print("Ano: " + str(carro.get_ano()))
            print("Placa: " + carro.get_placa())
            print("Quilometraegem: " + str(carro.get_quilometragem()))
            print("Diária: " + str(carro.get_diaria()))
            print("Seguro: " + str(carro.get_seguro()))

            print(("[1] Veículo anterior " if opcao > 0 else "") + ("[2] Próximo veículo " if opcao < self.carros.tam() else "") + "[9] Sair")
            

            match input("Selecione uma opcao"):

                case "1":
                    if opcao > 0:
                        opcao += 1
                    else:
                        print("Não há veículo anteriror")
                case "2":
                    if opcao < self.carros.tam():
                        opcao -=1
                    else:
                        print("Não há mais carros")
                case "9":
                    return
                case _:
                    print("Opção inválida!")
    

    




            
        









