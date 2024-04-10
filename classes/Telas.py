from classes.Carros import *
from classes.Locacoes import *
from classes.Clientes import *
import os
limpar_tela = "cls" if os.name == "nt" else os.system("clear")


class Telas:

    def __init__(self, caminho_locacoes, caminho_clientes, caminho_carros):
        self.locacoes = Locacoes(caminho_locacoes)
        self.clientes = Clientes(caminho_clientes)
        self.carros = Carros(caminho_carros)

    @staticmethod
    def limpar_tela():
        os.system(limpar_tela)

    def tela_inicial(self):

        while True:
            self.limpar_tela()

            print(
                f"[1] Locações\n" +
                "[2] Clientes\n" +
                "[3] Carros\n" +
                "[9] Sair\n\n\n"
            )

            match input("Digite a opção desejada: "):
                case "1":
                    self.tela_locacoes()
                case "2":
                    self.tela_clientes()
                case "3":
                    self.tela_carros()
                case "9":
                    return
                case _:
                    input("Opção inválida. Aperte [ENTER] para continuar")
        
    def tela_locacoes(self):
        while True: 
            self.limpar_tela()

            print(
                f"[1] Nova locação\n" +
                "[2] Finalizar Locação\n" +
                "[3] Relatório de carros locados\n" +
                "[9] Sair\n\n\n"
            )

            match input("Digite a opção desejada: "):
                case "1":
                    self.nova_locacao()
                case "2":
                    self.finalizar_locacao()
                case "3":
                    self.gerar_relatorio()
                case "9":
                    return
                case _:
                    input("Opção inválida. Aperte [ENTER] para continuar")
    
    def tela_clientes(self):
        while True:
            self.limpar_tela()
            
            print(
                f"[1] Cadastrar novo\n" +
                "[2] Atualizar informações\n" +
                "[3] Localizar locações\n" +
                "[9] Sair\n\n\n"
            )

            match input("Digite a opção desejada: "):
                case "1":
                    self.cadastrar_cliente()
                case "2":
                    self.atualizar_cliente()
                case "3":
                    self.localizar_locacoes()
                case "9":
                    return
                case _:
                    input("Opção inválida. Aperte [ENTER] para continuar")

    def tela_carros(self):

        while True:

            self.limpar_tela()

            print(
                f"[1] Cadastrar novo\n" +
                "[2] Atualizar informações\n" +
                "[3] Excluir um carro\n" +
                "[4] Disponibilizar carros para venda\n" +
                "[5] Localizar carros por categoria\n" +
                "[9] Sair\n"
            )

            match input("Digite a opção desejada: "):
                case "1":
                    self.cadastrar_carro()
                case "2":
                    self.atualizar_carro()
                case "5":
                    self.localiza_carro()
                case "9":
                    return
                case _:
                    input("Opção inválida. Aperte [ENTER] para continuar")

    def nova_locacao(self):
        self.limpar_tela()
        locacao = Locacao(vazio=True)
        carro = Carro(vazio=True)
        while True:
            try:
                cliente = self.clientes.get_cliente(input("Digite seu CPF: "))
                self.limpar_tela()
                break
            except IndexError:
                self.limpar_tela()
                input(f"Cliente não cadastrado, cadastre-se primeiro\nAperte [ENTER] para continuar")
            except ValueError:
                self.limpar_tela()
                print("CPF inválido.")
        while True:
            try:
                carro.set_categoria(input("Qual categoria de carro deseja? "))
                self.limpar_tela()
                break
            except ValueError:
                self.limpar_tela()
                print("Categoria inválida!")
        while True:
            try:
                carro.set_cambio(input("Qual tipo de cambio deseja? "))
                self.limpar_tela()
                break
            except ValueError:
                self.limpar_tela()
                print("Cambio inválido!")

        while True:
            seguro = input("Deseja adicionar seguro na locação? ")
            if seguro.upper() in ("SIM", "NÃO", "NAO"):
                seguro = seguro.upper() == "SIM"
                break
            print("Opção inválida!")

        try:
            ids = []

            for i in self.carros.get_id_categoria(carro.get_cambio(), carro.get_categoria()):
                if self.carros.get_carro(i).is_disponivel():
                    ids.append(i)

            if len(ids) == 0:
                raise IndexError("Nenhum carro disponível")

        except IndexError:
            self.limpar_tela()
            input(f"Nenhum carro disponível correspondente aos parâmetros definidos encontrado.\n"
                  f"Aperte [ENTER] para continuar")
            return

        opcao = 0
        while True:
            carro = self.carros.get_carro(ids[opcao])

            self.show_carro(carro, opcao + 1, len(ids), seguro)

            print(("[1] Veículo anterior " if opcao > 0 else "") +
                  "[3] Selecionar carro " +
                  ("[2] Próximo veículo " if opcao < len(ids) - 1 else "") +
                  "[9] Cancelar locação")

            match input(""):
                case "1":
                    if opcao > 0:
                        opcao -= 1
                    self.limpar_tela()
                case "2":
                    if opcao < len(ids) - 1:
                        opcao += 1
                    self.limpar_tela()
                case "3":
                    break
                case "9":
                    return
                case _:
                    self.limpar_tela()
                    pass

        locacao.set_id_carro(carro.get_id())
        locacao.set_cpf_cliente(cliente.get_cpf())
        locacao.set_km_inicial(carro.get_quilometragem())
        locacao.set_seguro("sim" if seguro else "não")
        carro.set_disponivel(False)
        self.locacoes.add_locacao(locacao)
        self.carros.salvar_csv()

    def finalizar_locacao(self):
        self.limpar_tela()
        while True:
            locacao = input("Digite o id da locação: ")
            if locacao.isnumeric():
                locacao = int(locacao)
                if locacao < self.locacoes.tam():
                    locacao = self.locacoes.get_locacao(locacao)
                    self.limpar_tela()
                    break
            self.limpar_tela()
            print("ID de locação inválido, tente novamente.")

        while True:
            data_devolucao = input(f"Digite a data e hora da devolução no formato DD/MM/AAAA HH:MM\n"
                                   f"Deixe em branco para definir a data e hora como a data e hora atuais\n")

            if data_devolucao == "":
                data_devolucao = datetime.now().strftime('%d/%m/%Y %H:%M')
                self.limpar_tela()
                break
            if (
                data_devolucao[0:2].isnumeric() and
                data_devolucao[3:5].isnumeric() and
                data_devolucao[6:8].isnumeric() and
                data_devolucao[11:13].isnumeric() and
                data_devolucao[14:16].isnumeric()
            ):
                self.limpar_tela()
                break
            self.limpar_tela()
            print("Data inválida. Tente novamente.")

        while True:
            try:
                quilometragem_devolucao = int(input(
                    f"Quilometragem no momento da locacao: {locacao.get_km_inicial()}\n"
                    f"Digite a quilometragem no momento da devolucao: "
                ))
                if quilometragem_devolucao < locacao.get_km_inicial():
                    raise ValueError("KM final não pode ser menor que KM inicial")
                self.limpar_tela()
                break
            except ValueError:
                self.limpar_tela()
                print("Quilometragem inválida, tente novamente.")

        carro = self.carros.get_carro(locacao.get_id_carro())
        try:
            valor_total = Locacoes.calcula_valor(
                carro.get_diaria(),
                carro.get_seguro() if locacao.get_seguro() else 0,
                locacao.get_data_locacao(),
                data_devolucao
            )
        except ValueError as e:
            if str(e) == "Não é possível calcular a diaria total para uma locação de menos de 24 horas":
                print("Não é possível devolver um carro com menos de 24 horas de locação.")
                input("Pressione ENTER para continuar...")
                return
            print(str(e))
            input("Pressione ENTER para continuar...")
            return
        locacao.set_data_devolucao(data_devolucao)
        locacao.set_km_final(quilometragem_devolucao)
        locacao.set_valor_total(valor_total)
        carro.set_quilometragem(quilometragem_devolucao)
        carro.set_disponivel(True)
        self.carros.salvar_csv()
        self.locacoes.salvar_csv()

    def gerar_relatorio(self):
        self.limpar_tela()
        locacoes_ativas = []
        for locacao in self.locacoes.get_lista():
            if locacao.get_data_devolucao() == "00/00/00 00:00":
                locacoes_ativas.append(locacao)

        header = ("CPF", "Nome", "Inicio", "Carro", "Categoria", "Placa", "Valor")
        tamanhos = (15, 30, 20, 10, 15, 10, 12)
        print(f"|{header[0][:tamanhos[0]]:<{tamanhos[0]}}|"
              f"{header[1][:tamanhos[1]]:<{tamanhos[1]}}|"
              f"{header[2][:tamanhos[2]]:<{tamanhos[2]}}|"
              f"{header[3][:tamanhos[3]]:<{tamanhos[3]}}|"
              f"{header[4][:tamanhos[4]]:<{tamanhos[4]}}|"
              f"{header[5][:tamanhos[5]]:<{tamanhos[5]}}|"
              f"{header[6][:tamanhos[6]]:<{tamanhos[6]}}|")

        print("=" * (sum(tamanhos) + len(tamanhos) + 1))

        for locacao in locacoes_ativas:
            cliente = self.clientes.get_cliente(locacao.get_cpf_cliente())
            carro = self.carros.get_carro(locacao.get_id_carro())
            try:
                valor_atual = Locacoes.calcula_valor(
                    carro.get_diaria(),
                    carro.get_seguro() if locacao.get_seguro() else 0,
                    locacao.get_data_locacao(),
                    datetime.now().strftime('%d/%m/%Y %H:%M')
                )
            except ValueError:
                valor_atual = 0

            valor_atual = "R$" + f"{valor_atual:.2f}".replace(".", ",")
            print(
                f"|{locacao.get_cpf_cliente()[:tamanhos[0]]:<{tamanhos[0]}}|" +
                f"{cliente.get_nome()[:tamanhos[1]]:<{tamanhos[1]}}|" +
                f"{locacao.get_data_locacao()[:tamanhos[2]]:<{tamanhos[2]}}|" +
                f"{carro.get_modelo()[:tamanhos[3]]:<{tamanhos[3]}}|" +
                f"{carro.get_categoria()[:tamanhos[4]]:<{tamanhos[4]}}|" +
                f"{carro.get_placa()[:tamanhos[5]]:<{tamanhos[5]}}|" +
                f"{valor_atual[:tamanhos[6]]:<{tamanhos[6]}}|"
            )
            input()

    def cadastrar_cliente(self):
        novo_cliente = Cliente(vazio=True)

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
                novo_cliente.set_idade(int(input("Digite sua idade: ")))
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
        self.clientes.salvar_csv()
        print("Cliente cadastrado com sucesso!")
        input("Aprente [ENTER] para continuar")
        return

    def atualizar_cliente(self):

        self.limpar_tela()

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
                f"[1] Nome\n" +
                "[2] Idade\n" +
                "[3] Endereço\n" +
                "[4] Cidade\n" +
                "[5] Estado\n" +
                "[9] Salvar e sair\n"
            )

            opcao = int(input("Selecione o dado que deseja alterar: "))    
            self.limpar_tela()

            match opcao:

                case 1:
                    cliente.set_nome(input("Digite o novo nome"))
                    self.limpar_tela()
                case 2:
                    try:
                        cliente.set_idade(int(input("Digite a nova idade")))
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

    def localizar_locacoes(self):
        self.limpar_tela()
        while True:
            identificacao = input("Digite o nome completo ou CPF do cliente que deseja localizar as locações: ")
            try:
                Cliente.formatar_cpf(identificacao)
            except ValueError:
                print("CPF")
            try:
                cliente = self.clientes.get_cliente(identificacao, identificacao)
            except IndexError:
                self.limpar_tela()
                input("Cliente não cadastrado. Aperte [ENTER] para continuar")









    def cadastrar_carro(self):

        novo_carro = Carro(vazio=True)

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
                novo_carro.set_ano(int(input("Digite o ano de lançamento do seu carro: ")))
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
                novo_carro.set_quilometragem(int(input("Digite a quilometragem do seu carro: ")))
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
                novo_carro.set_disponivel(input("O carro está disponível? "))
                self.limpar_tela()
                break
            except ValueError:
                self.limpar_tela()
                print(f"Valor inválido\nValores válidos: [Sim], [Não]")

        self.carros.add_carro(novo_carro)
        self.carros.salvar_csv()
        print("Carro cadastrado com sucesso!")
        input("Aperte [ENTER] para continuar")
        return
    
    def atualizar_carro(self):

        self.limpar_tela()
        carro = self.carros.get_carro(int(input("Digite o ID do carro que deseja alterar informações: ")))
        while True:
            self.limpar_tela()
            print(
                f"[1] Modelo\n" +
                "[2] Cor\n" +
                "[3] Ano\n" +
                "[4] Placa\n" +
                "[5] Cambio\n" +
                "[6] Categoria\n" +
                "[7] Quilometragem\n" +
                "[8] Aluguel\n" +
                "[9] Seguro\n" +
                "[10] Disponibilidade\n" +
                "[0] Salvar e sair\n"
            )

            match input("Selecione o que deseja alterar: "):
                case "1":
                    self.limpar_tela()
                    try:
                        carro.set_modelo(input("Digite o novo modelo do carro: "))
                    except ValueError:
                        input("Modelo inválido! Aperte [ENTER] para continuar")

                case "2":
                    self.limpar_tela()
                    try:
                        carro.set_cor(input("Digite a nova cor do carro: "))
                    except ValueError:
                        input("Cor inválida! Aperte [ENTER] para continuar")

                case "3":
                    self.limpar_tela()
                    try:
                        carro.set_ano(int(input("Digite o novo ano do carro: ")))
                    except ValueError:
                        input("Ano inválido! Aperte [ENTER] para continuar")
                        
                case "4":
                    self.limpar_tela()
                    try:
                        carro.set_placa(input("Digite a nova placa do carro: "))
                    except ValueError:
                        input("Placa inválida! Aperte [ENTER] para continuar")

                case "5":
                    self.limpar_tela()
                    try:
                        carro.set_cambio(input("Digite o novo câmbio do carro: "))
                    except ValueError:
                        input("Câmbio inválido! Aperte [ENTER] para continuar")

                case "6":
                    self.limpar_tela()
                    try:
                        carro.set_categoria(input("Digite a nova categoria do carro: "))
                    except ValueError:
                        input("Categoria inválida! Aperte [ENTER] para continuar")

                case "7":
                    self.limpar_tela()
                    try:
                        carro.set_quilometragem(int(input("Digite o nova quilometragem do carro: ")))
                    except ValueError:
                        input("Quilometragem inválida! Aperte [ENTER] para continuar")

                case "8":
                    self.limpar_tela()
                    try:
                        carro.set_diaria(input("Digite o novo valor de diária do carro: "))
                    except ValueError:
                        input("Diária inválida! Aperte [ENTER] para continuar")

                case "9":
                    self.limpar_tela()
                    try:
                        carro.set_seguro(input("Digite o novo valor de seguro do carro: "))
                    except ValueError:
                        input("Seguro inválido! Aperte [ENTER] para continuar")

                case "10":
                    self.limpar_tela()
                    try:
                        carro.set_disponivel(input("Digite a disponibilidade do carro (Sim ou não): "))
                    except ValueError:
                        input("Disponibilidade inválida! Aperte [ENTER] para continuar")

                case "0":
                    self.carros.salvar_csv()
                    return

                case _:
                    self.limpar_tela()
                    input("Opção inválida. Aperte [ENTER] para continuar")

    def localiza_carro(self):

        self.limpar_tela()

        while True:
            try:
                carro_a_encontrar = Carro(vazio=True)
                carro_a_encontrar.set_cambio(input("Digite o câmbio do seu carro: "))
                carro_a_encontrar.set_categoria(input("Digite a categoria do seu carro: "))
                ids = self.carros.get_id_categoria(carro_a_encontrar.get_cambio(), carro_a_encontrar.get_categoria())
                break

            except ValueError:
                print("Câmbio ou categoria inválidos!")
            except IndexError:
                input("Nenhum carro com os parâmetros especificados encontrado. Aperte [ENTER] para continuar")
                return

        opcao = 0

        while True:
            carro = self.carros.get_carro(ids[opcao])

            self.show_carro(carro, opcao + 1, len(ids))

            print(("[1] Veículo anterior " if opcao > 0 else "") +
                  ("[2] Próximo veículo " if opcao < len(ids) - 1 else "") +
                  "[9] Sair")

            match input(""):
                case "1":
                    if opcao > 0:
                        opcao -= 1
                    self.limpar_tela()
                case "2":
                    if opcao < len(ids) - 1:
                        opcao += 1
                    self.limpar_tela()
                case "9":
                    return
                case _:
                    self.limpar_tela()
                    pass

    @staticmethod
    def show_carro(carro, carro_atual, total_carros, mostrar_seguro=True):
        print("Modelo: " + carro.get_modelo())
        print("Cor: " + carro.get_cor())
        print("Ano: " + str(carro.get_ano()))
        print("Placa: " + carro.get_placa())
        print("Quilometraegem: " + str(carro.get_quilometragem()))
        print("Diária: " + str(carro.get_diaria()))
        if mostrar_seguro:
            print("Seguro: " + str(carro.get_seguro()))
        print("Mostrando " + str(carro_atual) + " de " + str(total_carros) + " carros correspondentes")
