import csv
import os


class Cliente:
    """
    Classe que representa um único cliente.
    Todos os atributos são privados, como denota o prefixo "__".
    Getters e setters devem ser usados para manipular os atributos.

    Atributos:
    __________
        __cpf: str = CPF do cliente, formatado como XXX.XXX.XXX-XX

        __nome: str = Nome do cliente

        __idade: int = Idade do cliente

        __endereco: str = Endereco do cliente

        __cidade: str = Cidade do cliente

        __estado: str = Estado do cliente
    """
    __cpf: str | None = None
    __nome: str | None = None
    __idade: int | None = None
    __endereco: str | None = None
    __cidade: str | None = None
    __estado: str | None = None
    __pai = None

    def set_pai(self, pai) -> None:
        """
        Define uma referência para o objeto de qual o objeto Cliente será dependente
        :param pai: Objeto de qual será dependente
        :type pai: Clientes
        :return: None
        :rtype: None
        """
        if type(pai) is not Clientes:
            raise TypeError("O objeto deve ser do tipo Clientes")
        self.__pai = pai

    def get_pai(self):
        """
        Retorna referência para o objeto de qual o objeto Cliente depende
        :return: Objeto pai
        :rtype: Clientes
        """
        return self.__pai

    def set_cpf(self, novo_cpf: str) -> None:
        """
        Define um CPF, desde que o mesmo seja válido
        :param novo_cpf: CPF para o qual se deseja mudar
        :return: None
        :rtype: None
        """
        self.__cpf = self.formatar_cpf(novo_cpf)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    @staticmethod
    def formatar_cpf(cpf: str | int) -> str:
        """
        Formata um CPF no formato XXX.XXX.XXX-XX, garantindo que ele seja válido
        :param cpf: CPF que se deseja formatar/checar validade
        :type cpf: str | int
        :return: CPF no formato XXX.XXX.XXX-XX
        :rtype: str
        """
        cpf = str(cpf).replace(".", "").replace("-", "")
        if len(cpf) != 11 or (not cpf.isnumeric()):
            print("pipipipopopo")
            raise ValueError("CPF inválido")
        if not cpf.isnumeric():
            raise ValueError("CPF inválido")
        resto_primeira = (
                (
                        int(cpf[0]) * 10 +
                        int(cpf[1]) * 9 +
                        int(cpf[2]) * 8 +
                        int(cpf[3]) * 7 +
                        int(cpf[4]) * 6 +
                        int(cpf[5]) * 5 +
                        int(cpf[6]) * 4 +
                        int(cpf[7]) * 3 +
                        int(cpf[8]) * 2
                ) % 11
        )
        resto_segunda = (
                (
                        int(cpf[0]) * 11 +
                        int(cpf[1]) * 10 +
                        int(cpf[2]) * 9 +
                        int(cpf[3]) * 8 +
                        int(cpf[4]) * 7 +
                        int(cpf[5]) * 6 +
                        int(cpf[6]) * 5 +
                        int(cpf[7]) * 4 +
                        int(cpf[8]) * 3 +
                        int(cpf[9]) * 2
                ) % 11
        )
        if (
                (resto_primeira <= 1 and int(cpf[9]) != 0) or
                (resto_segunda <= 1 and int(cpf[10]) != 0)
        ):
            print("erro1")
            raise ValueError("CPF inválido")
        if (
                (resto_primeira > 1 and 11 - resto_primeira != int(cpf[9])) or
                (resto_segunda > 1 and 11 - resto_segunda != int(cpf[10]))
        ):
            raise ValueError("CPF inválido")
        cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        return cpf

    def get_cpf(self) -> str:
        """
        Retorna o CPF do cliente
        :return: CPF
        :rtype: str
        """
        return self.__cpf

    def set_nome(self, novo_nome: str) -> None:
        """
        Define o nome do cliente
        :param novo_nome: Nome para o qual deseja ser definido
        :type novo_nome:  str
        :return: None
        :rtype: None
        """
        self.__nome = str(novo_nome)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_nome(self) -> str:
        """
        Retorna o nome do cliente
        :return: Nome do cliente
        :rtype: str
        """
        return self.__nome

    def set_idade(self, nova_idade: int) -> None:
        """
        Define o idade do cliente
        :param nova_idade: Idade para a qual deve ser definida
        :return: None
        :rtype: None
        """
        nova_idade = int(nova_idade)
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa")
        self.__idade = nova_idade
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_idade(self) -> int:
        """
        Retorna o idade do cliente
        :return: Idade do cliente
        :rtype: int
        """
        return self.__idade

    def set_endereco(self, novo_endereco: str) -> None:
        """
        Define o endereco do cliente
        :param novo_endereco: Endereço para o qual deve ser definido
        :return: None
        :rtype: None
        """
        self.__endereco = str(novo_endereco)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_endereco(self) -> str:
        """
        Retorna o endereco do cliente
        :return: Endereço do cliente
        :rtype: str
        """
        return self.__endereco

    def set_cidade(self, nova_cidade: str) -> None:
        """
        Define a cidade do cliente
        :param nova_cidade: Cidade para a qual deve ser definida
        :return: None
        :rtype: None
        """
        self.__cidade = str(nova_cidade)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_cidade(self) -> str:
        """
        Retorna a cidade do cliente
        :return: Cidade do cliente
        :rtype: str
        """
        return self.__cidade

    def set_estado(self, novo_estado: str) -> None:
        """
        Define o estado do cliente
        :param novo_estado: Estado para o qual deve ser definido
        :return: None
        :rtype: None
        """
        self.__estado = str(novo_estado)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_estado(self) -> str:
        """
        Retorna o estado do cliente
        :return: Estado do cliente
        :rtype: str
        """
        return self.__estado

    def __init__(
        self,
        cpf: str = None,
        nome: str = None,
        idade: int = None,
        endereco: str = None,
        cidade: str = None,
        estado: str = None,
        pai=None,
        vazio: bool = False
    ) -> None:
        """
        Inicializa um objeto Cliente e todos seus atributos,
        ou inicializa um objeto Cliente vazio se vazio=True
        :param cpf: CPF do cliente, formatado ou não
        :type cpf: str
        :param nome: Nome do cliente
        :type nome: str
        :param idade: Idade do cliente
        :type idade: int
        :param endereco: Endereco do cliente
        :type endereco: str
        :param cidade: Cidade do cliente
        :type cidade: str
        :param estado: Estado do cliente
        :type estado: str
        :param pai: Objeto Clientes a qual o objeto Cliente é associado
        :type pai: Clientes | None
        :param vazio: Deve ser definido como True caso deseje iniciar um objeto vazio
        :type vazio: bool
        """
        if not vazio:
            self.set_cpf(cpf)
            self.set_nome(nome)
            self.set_idade(idade)
            self.set_endereco(endereco)
            self.set_cidade(cidade)
            self.set_estado(estado)
            self.__pai = pai

    def get_linha(self) -> tuple:
        """
        Retorna uma tupla com os atributos do cliente.
        Usado em conjunto com csv.writer.writerow()
        :return: Tupla com os atributos do cliente
        :rtype: tuple
        """
        return (
            self.get_cpf(),
            self.get_nome(),
            self.get_idade(),
            self.get_endereco(),
            self.get_cidade(),
            self.get_estado()
        )

    def is_valido(self) -> bool:
        """
        Verifica se o objeto Cliente é válido (Tem todos os atributos) e pode ser salvo
        :return: True se o objeto Cliente for válido, False se o objeto Cliente for inválido
        :rtype: bool
        """
        if (
            self.get_cpf() is None or
            self.get_nome() is None or
            self.get_idade() is None or
            self.get_endereco() is None or
            self.get_cidade() is None or
            self.get_estado() is None
        ):
            return False
        return True


class Clientes:
    """
    Classe que organiza o arquivo CSV clientes em uma lista de clientes e fornece métodos para manipulação da mesma.
    Atributos com o prefixo "__" são privados e não devem ser manipulados diretamente

    Atributos:
    __________
        novo_cliente: Cliente = Novo cliente vazio, para ser preenchido e adicionado à lista

        __lista: dict[str, Cliente] = Lista de todos os clientes. carregada a partir do arquivo fornecido no construtor

        __salvo: bool = True se as informações do arquivo estiverem sincronizadas com as informações da lista

        __caminho_para_arquivo = Caminho do arquivo CSV de onde devem ser carregadas a lista e onde deve ser salva

    """
    __lista: dict[str, Cliente] = {}
    __salvo: bool = False
    __caminho_para_arquivo: str | None = None

    def __init__(self, caminho_para_arquivo: str) -> None:
        """
        Inicializa o objeto Clientes, carregando suas informações a partir do arquivo que está no caminho
        "caminho_para_arquivo".
        Se o diretório, arquivo ou ambos não existirem, serão criados.
        :param caminho_para_arquivo: Caminho para o arquivo .csv onde estão armazenadas as informações dos clientes
        :type caminho_para_arquivo: str
        """
        diretorio, arquivo = os.path.split(caminho_para_arquivo)
        if not os.path.isdir(diretorio):
            os.makedirs(diretorio)
            if not os.path.isdir(diretorio):
                raise ValueError("Caminho inválido")

        self.__caminho_para_arquivo = caminho_para_arquivo

        try:
            with (open(self.__caminho_para_arquivo, newline="") as arquivo):
                arquivo_csv = csv.reader(arquivo, delimiter=";")
                next(arquivo_csv, None)

                for linha in arquivo_csv:
                    self.__lista[linha[0]] = Cliente(
                                                linha[0],
                                                linha[1],
                                                int(linha[2]),
                                                linha[3],
                                                linha[4],
                                                linha[5],
                                                self
                                            )

        except FileNotFoundError:
            with open(self.__caminho_para_arquivo, "w", newline="") as arquivo:
                escritor = csv.writer(arquivo, delimiter=";")
                escritor.writerow(["CPF", "Nome", "Idade", "Endereço", "Cidade", "Estado"])

        self.__salvo = True

    def salvar_csv(self) -> None:
        """
        Salva o arquivo CSV caso o mesmo tenha sido modificado.
        :return: None
        :rtype: None
        """

        with open(self.__caminho_para_arquivo, 'w', newline="") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(
                (
                    "CPF",
                    "Nome",
                    "Idade",
                    "Endereço",
                    "Cidade",
                    "Estado"
                )
            )

            for item in self.__lista.values():
                escritor.writerow(item.get_linha())
            self.__salvo = True

    def add_cliente(self, novo_cliente: Cliente) -> None:
        """
        Adiciona o Cliente "novo_cliente" a lista de clientes e gera um novo cliente vazio em "novo_cliente"
        :param novo_cliente: Novo cliente a ser adicionado na lista de clientes
        :return: None
        :rtype: None
        :raises Exception: Se o cliente não for válido será gerado um erro
        """
        if not novo_cliente.is_valido():
            raise Exception("Informações faltando no novo cliente")
        self.__lista[novo_cliente.get_cpf()] = novo_cliente
        self.__salvo = False

    def get_cliente(self, cpf: str) -> Cliente:
        """
        Retorna a referência para um objeto Cliente.
        Pode ser usado tanto para ler quanto para modificar o objeto cliente
        :param cpf: CPF do cliente que deseja, formatado ou não
        :type cpf: str
        :return: Cliente com CPF correspondente
        :rtype: Cliente
        """
        cpf = Cliente.formatar_cpf(cpf)
        if cpf not in self.__lista:
            raise Exception("Cliente não cadastrado")
        return self.__lista[cpf]

    def set_salvo(self, salvo: bool):
        if type(salvo) is not bool:
            raise TypeError("salvo deve ser do tipo bool")
        self.__salvo = salvo

    def is_salvo(self) -> bool:
        """
        Verifica se a lista está sincronizada com o arquivo CSV
        :return: True se estiver sincronizada, False caso contrário
        :rtype: bool
        """
        return self.__salvo
