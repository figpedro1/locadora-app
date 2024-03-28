import os
import csv
import datetime


class Carro:
    """
    Classe que representa um carro.
    Atributos com prefixo "__" não devem ser acessados diretamente. Use os getters e setters correspondentes.

    Atributos:
    ----------
        __id: int = ID do carro.

        __modelo: str = "Kwid", "Polo", "Rengegade", "T-Cross", "Corolla" ou "Hilux".

        __cor: str = "Preto" ou "Cinza"

        __ano: int = Ano do carro

        __placa: str = Placa do carro no formato XXX-XXXX

        __cambio: str = "Manual" ou "Automático"

        __categoria: str = "Econômico", "Intermediário", "Conforto" ou "Pickup".

        __quilometragem: int = Quilometragem do carro

        __aluguelPorDia: float = Valor do aluguel do carro (por dia)

        __seguroPorDia: float = Valor do seguro do carro (por dia)

        __disponivel: bool = True se o carro estiver disponível, False caso contrário

        __pai: Carros = Objeto Carros a qual está associada
    """
    __id: int | None = None
    __modelo: str | None = None
    __cor: str | None = None
    __ano: int | None = None
    __placa: str | None = None
    __cambio: str | None = None
    __categoria: str | None = None
    __quilometragem: int | None = None
    __aluguelPorDia: float | None = None
    __seguroPorDia: float | None = None
    __disponivel: bool | None = None
    __pai: None = None

    def get_pai(self):
        return self.__pai

    def set_id(self, novo_id: int) -> None:
        """
        Define o ID do carro
        :param novo_id: ID para o qual deve ser definido
        :type novo_id: int
        :return: None
        :rtype: None
        :raises ValueError: Caso o novo_id não for um número inteiro
        """
        self.__id = int(novo_id)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_id(self) -> int:
        """
        Retorna o ID do carro
        :return: ID do carro
        :rtype: int
        """
        return self.__id

    def set_modelo(self, novo_modelo: str) -> None:
        """
        Define o modelo do carro, entre os modelos válidos
        :param novo_modelo: "Kwid", "Polo", "Rengegade", "T-Cross", "Corolla" ou "Hilux". Não é case-sensitive
        :type novo_modelo: str
        :return: None
        :rtype: None
        :raises ValueError: Caso o modelo não esteja entre os modelos aceitos
        """
        if novo_modelo.upper() not in ("KWID", "POLO", "RENEGADE", "T-CROSS", "COROLLA", "HILUX"):
            raise ValueError("Modelo inválido")
        self.__modelo = novo_modelo.capitalize()
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_modelo(self) -> str:
        """
        Retorna o modelo do carro.
        :return: Modelo do carro
        :rtype: str
        """
        return self.__modelo

    def set_cor(self, nova_cor: str) -> None:
        """
        Define a cor do carro, entre as cores válidas
        :param nova_cor: "Preto" ou "Cinza". Não é case-sensitive
        :type nova_cor: str
        :return: None
        :rtype: None
        :raises ValueError: Caso a cor do carro não seja válida
        """
        if nova_cor.upper() not in ("PRETO", "CINZA"):
            raise ValueError("Cor inválida")
        self.__cor = nova_cor.capitalize()
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_cor(self) -> str:
        """
        Retorna a cor do carro
        :return: Cor do carro
        :rtype: str
        """
        return self.__cor

    def set_ano(self, novo_ano: int) -> None:
        """
        Define o ano do carro :param novo_ano: O ano para o qual deve ser definido :type novo_ano: int :return: None
        :rtype: None :raises ValueError: Caso novo_ano não seja um inteiro, novo_ano < 1886 (ano que o primeiro carro
        saiu) ou novo_ano > ano atual + 1
        """
        novo_ano = int(novo_ano)
        # Segundo o google, o primeiro carro surgiu em 1886, e o carro mais recente que pode ser comprado sempre é o
        # do ano atual + 1
        if novo_ano > datetime.datetime.now().year + 1 or novo_ano < 1886:
            raise ValueError("Ano inválido")
        self.__ano = novo_ano
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_ano(self) -> int:
        """
        Retorna o ano do carro
        :return: Ano do carro
        :rtype: int
        """
        return self.__ano

    def set_placa(self, nova_placa: str) -> None:
        """
        Define a placa do carro, desde que a mesma seja válida.
        :param nova_placa: Placa do carro no formato AAANNNN ou AAA-NNNN, onde A = Letra e N = Número
        :type nova_placa: str
        :return: None
        :rtype: None
        :raises ValueError: Caso a placa for inválida
        """
        nova_placa = str(nova_placa)
        tamanho = len(nova_placa)
        tamanho_valido = tamanho == 7 or tamanho == 8
        primeira_parte_valida = nova_placa[:3].isalpha()
        segunda_parte_valida = nova_placa[tamanho - 4: tamanho].isdigit()
        placa_valida = tamanho_valido and primeira_parte_valida and segunda_parte_valida
        if not placa_valida:
            raise ValueError("Placa inválida")
        nova_placa = "{}-{}".format(nova_placa[:3], nova_placa[len(nova_placa) - 4:len(nova_placa)].upper())
        self.__placa = nova_placa
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_placa(self) -> str:
        """
        Retorna a placa do carro
        :return: Placa do carro no formato AAA-NNNN onde A = Letra e N = Número
        :rtype: string
        """
        return self.__placa

    def set_cambio(self, novo_cambio: str) -> None:
        """
        Define o tipo de cambio do carro
        :param novo_cambio: "Automático" ou "Manual", não é case-sensitive
        :type novo_cambio: str
        :return: None
        :rtype: None
        :raises ValueError: Caso o tipo de cambio seja inválido
        """
        if str(novo_cambio).upper() not in ("AUTOMATICO", "AUTOMÁTICO", "MANUAL"):
            raise ValueError("Cambio inválido")
        self.__cambio = "Automático" if str(novo_cambio).upper() in ("AUTOMATICO", "AUTOMÁTICO") else "Manual"
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_cambio(self) -> str:
        """
        Retorna o tipo de cambio do carro
        :return: Tipo de cambio do carro
        :rtype: str
        """
        return self.__cambio

    def set_categoria(self, nova_categoria: str) -> None:
        """
        Define o categoria do carro, desde que seja válida
        :param nova_categoria: "Econômico", "Intermediário", "Conforto" ou "Pickup". Não é case-sensitive
        :type nova_categoria: str
        :return: None
        :rtype: None
        :raises ValueError: Caso a categoria seja inválida
        """
        if str(nova_categoria).upper() not in ("ECONÔMICO", "ECONOMICO", "INTERMEDIÁRIO",
                                               "INTERMEDIARIO", "CONFORTO", "PICKUP"):
            raise ValueError("Categoria inválida: " + nova_categoria)

        if nova_categoria.upper() == "ECONOMICO":
            nova_categoria = "Econômico"

        if nova_categoria.upper() == "INTERMEDIARIO":
            nova_categoria = "Intermediário"

        self.__categoria = nova_categoria.capitalize()
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_categoria(self) -> str:
        """
        Retorna o categoria do carro
        :return: Categoria do carro
        :rtype: str
        """
        return self.__categoria

    def set_quilometragem(self, nova_quilometragem: int) -> None:
        """
        Define a quilometragem do veículo
        :param nova_quilometragem: Quilometragem do veículo >= 0
        :type nova_quilometragem: int
        :return: None
        :rtype: None
        :raises ValueError: Caso a quilometragem seja inválida
        """
        try:
            if int(nova_quilometragem) < 0:
                raise ValueError("Quilometragem inválida")
        except ValueError:
            raise ValueError("Quilometragem inválida")

        self.__quilometragem = int(nova_quilometragem)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_quilometragem(self) -> int:
        """
        Retorna a quilometragem do veículo
        :return: Quilometragem do veículo
        :rtype: int
        """
        return self.__quilometragem

    def set_diaria(self, nova_diaria: float | str) -> None:
        """
        Define o valor do aluguel diario do carro
        :param nova_diaria: Valor do aluguel, no formato xx,xx ou xx.xx
        :type nova_diaria: float | str
        :return: None
        :rtype: None
        """
        try:
            if type(nova_diaria) is str:
                nova_diaria = self.decimal_para_float(nova_diaria)

            if float(nova_diaria) < 0:
                raise ValueError("Valor para diária inválido")
        except ValueError:
            raise ValueError("Valor para diária inválido")

        self.__aluguelPorDia = float(nova_diaria)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_diaria(self) -> float:
        """
        Retorna o valor da diaria
        :return: Valor da diaria
        :rtype: float
        """
        return self.__aluguelPorDia

    def set_seguro(self, novo_seguro: float | str) -> None:
        """
        Define o valor do seguro por dia
        :param novo_seguro: Valor do seguro, no formato xx,xx ou xx.xx
        :type novo_seguro: float | str
        :return: None
        :rtype: None
        """
        try:
            if type(novo_seguro) is str:
                novo_seguro = self.decimal_para_float(novo_seguro)

            if float(novo_seguro) < 0:
                raise ValueError("Quilometragem inválida")
        except ValueError:
            raise ValueError("Quilometragem inválida")

        self.__seguroPorDia = float(novo_seguro)
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def get_seguro(self) -> float:
        """
        Retorna o valor do seguro por dia
        :return: Valor do seguro por dia
        :rtype: float
        """
        return self.__seguroPorDia

    def set_disponivel(self, novo_disponivel: bool | str) -> None:
        """
        Define se o carro está disponível para ser alugado
        :param novo_disponivel: "Sim", "Não", "True" ou "False". Não é case-sensitive
        :type novo_disponivel: bool | str
        :return: None
        :rtype: None
        :raises TypeError: Caso novo_disponivel seja inválido
        """
        try:
            if type(novo_disponivel) is str:
                novo_disponivel = True if (novo_disponivel.upper() == "TRUE" or
                                           novo_disponivel.upper() == "SIM") else False
            novo_disponivel = bool(novo_disponivel)
        except ValueError:
            raise TypeError("Valor inválido para disponível")

        self.__disponivel = novo_disponivel
        if self.get_pai() is not None:
            self.get_pai().set_salvo(False)

    def is_disponivel(self) -> bool:
        """
        Verifica se o veículo está disponível
        :return: True ou False
        :rtype: bool
        """
        return self.__disponivel

    def __init__(
        self,
        id_carro: int | None = None,
        modelo: str | None = None,
        cor: str | None = None,
        ano: int | None = None,
        placa: str | None = None,
        cambio: str | None = None,
        categoria: str | None = None,
        quilometragem: int | None = None,
        diaria: float | None = None,
        seguro: float | None = None,
        disponivel: bool | str | None = None,
        pai: object | None = None,
        vazio: bool = False
    ) -> None:
        """
        Inicializa um objeto Carro e seus atributos, ou
        inicializa um objeto Carro vazio se vazio=True
        :param id_carro: ID do carro
        :type id_carro: int | None
        :param modelo: "Kwid", "Polo", "Renegade", "T-Cross", "Corolla" ou "Hilux". Não é case-sensitive
        :type modelo: str | None
        :param cor: "Preto" ou "Cinza". Não é case-sensitive
        :type cor: str | None
        :param ano: Ano do carro
        :type ano: int | None
        :param placa: Placa do carro no formato XXXXXXX ou XXX-XXXX
        :type placa: str | None
        :param cambio: "Automático" ou "Manual". Não é case-sensitive
        :type cambio: str | None
        :param categoria: "Econômico", "Intermediário", "Conforto" ou "Pickup". Não é case-sensitive
        :type categoria: str | None
        :param quilometragem: Quilometragem do carro
        :type quilometragem: int | None
        :param diaria: Valor do aluguel diário do carro
        :type diaria: float | None
        :param seguro: Valor do seguro diário do carro
        :type seguro: float | None
        :param disponivel: "Sim", "Não", "True" ou "False". Não é case-sensitive
        :type disponivel: str | bool | None
        :param pai: Objeto a qual o objeto Carro está associado
        :type pai: Carros | None
        :param vazio: Se o objeto deve ser inicializado vazio defina como True
        :type vazio: bool
        """
        if not vazio:
            self.set_id(id_carro)
            self.set_modelo(modelo)
            self.set_cor(cor)
            self.set_ano(ano)
            self.set_placa(placa)
            self.set_cambio(cambio)
            self.set_categoria(categoria)
            self.set_quilometragem(quilometragem)
            self.set_diaria(diaria)
            self.set_seguro(seguro)
            self.set_disponivel(disponivel)
            self.__pai = pai

    @staticmethod
    def decimal_para_float(valor: str) -> float:
        """
        Transforma uma string com um valor decimal separado por "," em um float
        :param valor: Valor no formato xx,xx
        :type valor: str
        :return: Valor float
        :rtype: float
        """
        if type(valor) is not str:
            raise TypeError("Tipo inválido")
        novo_valor = valor.replace(',', '.')
        return float(novo_valor)

    def is_valido(self) -> bool:
        """
        Verifica se o objeto Carro é válido (Tem todos os campos preenchidos)
        :return: True se for válido e False se for inválido
        :rtype: bool
        """
        if (
                self.get_id() is None or
                self.get_modelo() is None or
                self.get_cor() is None or
                self.get_ano() is None or
                self.get_placa() is None or
                self.get_cambio() is None or
                self.get_categoria() is None or
                self.get_quilometragem() is None or
                self.get_diaria() is None or
                self.get_seguro() is None or
                self.is_disponivel() is None
        ):
            return False
        return True

    def get_linha(self) -> tuple:
        """
        Retorna uma tupla com os atributos do cliente.
        Usado em conjunto com csv.writer.writerow()
        :return: Tupla com os atributos do carro
        :rtype: tuple
        """
        return (
            self.get_id(),
            self.get_modelo(),
            self.get_cor(),
            self.get_ano(),
            self.get_placa(),
            self.get_cambio(),
            self.get_categoria(),
            self.get_quilometragem(),
            self.get_diaria(),
            self.get_seguro(),
            "Sim" if self.is_disponivel() else "Não"
        )


class Carros:
    """
    Uma lista de instâncias de Carro, geradas a partir de um arquivo CSV com os dados.

    Atributos:
    ----------
        __lista: list[Carro] = Lista de todas as instâncias de carro

        __salvo: bool = Indica se o arquivo está salvo

        __caminho_para_arquivo: str = Caminho para o arquivo CSV

        __novo_carro: Carro = Instância de carro vazio, para ser preenchido e adicionado ao CSV
    """
    __lista: list[Carro] = []
    __salvo: bool = False
    __caminho_para_arquivo: str = None
    __novo_carro: Carro = Carro(vazio=True)
    __id_por_classificacao: dict = {}

    def __init__(self, caminho_para_arquivo):
        diretorio, arquivo = os.path.split(caminho_para_arquivo)
        if not os.path.isdir(diretorio):
            os.makedirs(diretorio)
            if not os.path.isdir(diretorio):
                raise ValueError("Caminho inválido")

        self.__id_por_classificacao = {}

        try:
            with open(caminho_para_arquivo, 'r', newline="") as arquivo:
                arquivo_csv = csv.reader(arquivo, delimiter=";")
                next(arquivo_csv, None)

                for linha in arquivo_csv:
                    self.__lista.append(
                        Carro(
                            int(linha[0]),
                            linha[1],
                            linha[2],
                            int(linha[3]),
                            linha[4],
                            linha[5],
                            linha[6],
                            int(linha[7]),
                            float(linha[8]),
                            float(linha[9]),
                            bool(linha[10] == "Sim"),
                            self
                        )
                    )
                    if linha[5] not in self.__id_por_classificacao:
                        self.__id_por_classificacao[linha[5]] = {}
                    if linha[6] not in self.__id_por_classificacao[linha[5]]:
                        self.__id_por_classificacao[linha[5]][linha[6]] = []
                    self.__id_por_classificacao[linha[5]][linha[6]].append(int(linha[0]))

        except FileNotFoundError:
            with open(caminho_para_arquivo, 'w', newline="") as arquivo:
                escritor = csv.writer(arquivo, delimiter=";")
                escritor.writerow([
                    "Identificação do carro",
                    "Modelo",
                    "Cor",
                    "Ano de fabricação",
                    "Placa",
                    "Câmbio",
                    "Categoria",
                    "Quilometragem",
                    "Valor da diária",
                    "Valor do seguro por dia",
                    "Disponível"])
        self.__caminho_para_arquivo = caminho_para_arquivo
        self.__salvo = True

    def tam(self) -> int:
        return len(self.__lista)

    def get_carro(self, id_carro) -> Carro:
        if int(id_carro) > len(self.__lista) - 1:
            raise ValueError("Indíce inexistente")
        return self.__lista[id_carro]

    def get_novo_carro(self) -> Carro:
        return self.__novo_carro
    
    def zerar_novo_carro(self):
        self.__novo_carro = Carro(vazio=True)

    def add_carro(self):
        self.get_novo_carro().set_id(self.tam())
        self.get_novo_carro().__pai = self
        if not self.get_novo_carro().is_valido():
            raise ValueError("Declare todos os atributos do novo carro antes de adicioná-lo")
        self.__lista.append(self.get_novo_carro())
        self.zerar_novo_carro()
        self.__salvo = False

    def salvar_csv(self):
        if self.__salvo:
            return

        with open(self.__caminho_para_arquivo, 'w', newline="") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(
                (
                    "Identificação do Carro",
                    "Modelo",
                    "Cor",
                    "Ano de fabricação",
                    "Placa",
                    "Câmbio",
                    "Categoria",
                    "Quilometragem",
                    "Valor da diária",
                    "Valor do seguro por dia",
                    "Disponível"
                )
            )

            for item in self.__lista:
                escritor.writerow(item.get_linha())
            self.__salvo = True

    def get_id_categoria(self, cambio: str, categoria: str) -> list:
        """
        Retorna uma lista com o id de todos os carros que preenchem os requisitos de câmbio e categoria
        :param cambio: "Manual" ou "Automatico". Não é case-sensitive
        :type cambio: str
        :param categoria: "Econômico", "Intermediário", "Conforto" ou "Pickup". Não é case-sensitive
        :type categoria: str
        :return: Lista de inteiros com o id dos carros cumpram os requisitos
        :rtype: list
        """
        if cambio.upper() not in ("MANUAL", "AUTOMATICO", "AUTOMÁTICO"):
            raise ValueError("Cambio inválido: " + cambio)
        if categoria.upper() not in ("ECONÔMICO", "ECONOMICO", "INTERMEDIÁRIO", "INTERMEDIARIO", "CONFORTO", "PICKUP"):
            raise ValueError("Categoria inválida: " + categoria)
        cambio = ("Automático" if cambio.upper() == "AUTOMATICO" or cambio.upper() == "AUTOMÁTICO" else "Manual")
        if categoria.upper() == "INTERMEDIARIO":
            categoria = "Intermediário"
        if categoria.upper() == "ECONOMICO":
            categoria = "Econômico"
        cambio = cambio.capitalize()
        categoria = categoria.capitalize()

        if cambio not in self.__id_por_classificacao:
            raise IndexError("Nenhum carro com câmbio " + cambio.lower() + " encontrado.")
        if categoria not in self.__id_por_classificacao[cambio]:
            raise IndexError("Nenhum carro da categoria " + categoria.lower() + " encontrado.")

        return self.__id_por_classificacao[cambio][categoria]

    def set_salvo(self, salvo):
        self.__salvo = salvo
    
    def is_salvo(self):
        return self.__salvo
