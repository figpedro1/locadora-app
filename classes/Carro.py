import datetime


class Carro:
    __id = None
    __modelo = None
    __cor = None
    __ano = None
    __placa = None
    __cambio = None
    __categoria = None
    __quilometragem = None
    __aluguelPorDia = None
    __seguroPorDia = None
    __disponivel = None

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
        if nova_cor.upper() in ("PRETO", "CINZA"):
            raise ValueError("Cor inválida")
        self.__cor = nova_cor.capitalize()

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
            raise ValueError("Categoria inválida")

        if nova_categoria.upper() == "ECONOMICO":
            nova_categoria = "Econômico"

        if nova_categoria.upper() == "INTERMEDIARIO":
            nova_categoria = "Intermediário"

        self.__categoria = nova_categoria.capitalize()

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

            if "," in nova_diaria:
                nova_diaria = self.decimal_para_float(nova_diaria)

            if float(nova_diaria) < 0:
                raise ValueError("Valor para diária inválido")
        except ValueError:
            raise ValueError("Val1or para diária inválido inválido")

        self.__aluguelPorDia = float(nova_diaria)

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
            if "," in novo_seguro:
                novo_seguro = self.decimal_para_float(novo_seguro)

            if float(novo_seguro) < 0:
                raise ValueError("Quilometragem inválida")
        except ValueError:
            raise ValueError("Quilometragem inválida")

        self.__seguroPorDia = float(novo_seguro)

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

    @staticmethod
    def decimal_para_float(valor: str) -> float:
        """
        Transforma uma string com um valor decimal separado por "," em um float
        :param valor: Valor no formato xx,xx
        :type valor: str
        :return: Valor float
        :rtype: float
        """
        if not type(valor) is str:
            raise TypeError("Tipo inválido")
        novo_valor = valor.replace(',', '.')
        if not novo_valor.isnumeric():
            raise ValueError("Valor inválido")
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
