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
        try:
            self.__id = int(novo_id)
        except ValueError:
            raise TypeError('ID precisa ser um número inteiro')

    def get_id(self) -> int:
        return self.__id

    def set_modelo(self, novo_modelo: str) -> None:
        if novo_modelo.upper() not in ("KWID", "POLO", "RENEGADE", "T-CROSS", "COROLLA", "HILUX"):
            raise ValueError("Modelo inválido")
        novo_modelo = novo_modelo.capitalize()
        self.__modelo = novo_modelo

    def get_modelo(self) -> str:
        return self.__modelo

    def set_cor(self, nova_cor: str) -> None:
        if nova_cor.upper() in ("PRETO", "CINZA"):
            raise ValueError("Cor inválida")
        nova_cor = nova_cor.capitalize()
        self.__cor = nova_cor

    def get_cor(self) -> str:
        return self.__cor

    def set_ano(self, novo_ano: int) -> None:
        try:
            novo_ano = int(novo_ano)
        except ValueError:
            raise TypeError("Ano precisa ser um número inteiro")
        # Segundo o google, o primeiro carro surgiu em 1886, e o carro mais recente que pode ser comprado sempre é o
        # do ano atual + 1
        if novo_ano > datetime.datetime.now().year + 1 or novo_ano < 1886:
            raise ValueError("Ano inválido")
        self.__ano = novo_ano

    def get_ano(self) -> int:
        return self.__ano

    def set_placa(self, nova_placa: str) -> None:
        tamanho = len(str(nova_placa))
        tamanho_valido = tamanho == 7 or tamanho == 8
        primeira_parte_valida = nova_placa[0:3].isalpha()
        segunda_parte_valida = nova_placa[tamanho - 4: tamanho].isdigit()
        placa_valida = tamanho_valido and primeira_parte_valida and segunda_parte_valida
        if not placa_valida:
            raise ValueError("Placa inválida")
        self.__placa = nova_placa

    def get_placa(self) -> str:
        return self.__placa

    def set_cambio(self, novo_cambio: str) -> None:
        if str(novo_cambio).upper() not in ("AUTOMATICO", "AUTOMÁTICO", "MANUAL"):
            raise ValueError("Cambio inválido")
        self.__cambio = "Automático" if str(novo_cambio).upper() in ("AUTOMATICO", "AUTOMÁTICO") else "Manual"

    def get_cambio(self) -> str:
        return self.__cambio

    def set_categoria(self, nova_categoria: str) -> None:
        if str(nova_categoria).upper() not in ("ECONÔMICO", "ECONOMICO", "INTERMEDIÁRIO",
                                               "INTERMEDIARIO", "CONFORTO", "PICKUP"):
            raise ValueError("Categoria inválida")

        if nova_categoria.upper() == "ECONOMICO":
            nova_categoria = "Econômico"

        if nova_categoria.upper() == "INTERMEDIARIO":
            nova_categoria = "Intermediário"

        self.__categoria = nova_categoria.capitalize()

    def get_categoria(self) -> str:
        return self.__categoria

    def set_quilometragem(self, nova_quilometragem: int) -> None:
        try:
            if int(nova_quilometragem) < 0:
                raise ValueError("Quilometragem inválida")
        except ValueError:
            raise ValueError("Quilometragem inválida")

        self.__quilometragem = int(nova_quilometragem)

    def get_quilometragem(self) -> int:
        return self.__quilometragem

    def set_diaria(self, nova_diaria: float | str) -> None:
        try:

            if "," in nova_diaria:
                nova_diaria = self.decimal_para_float(nova_diaria)

            if float(nova_diaria) < 0:
                raise ValueError("Valor para diária inválido")
        except ValueError:
            raise ValueError("Val1or para diária inválido inválido")

        self.__aluguelPorDia = float(nova_diaria)

    def get_diaria(self) -> float:
        return self.__aluguelPorDia

    def set_seguro(self, novo_seguro: float | str) -> None:
        try:
            if "," in novo_seguro:
                novo_seguro = self.decimal_para_float(novo_seguro)

            if float(novo_seguro) < 0:
                raise ValueError("Quilometragem inválida")
        except ValueError:
            raise ValueError("Quilometragem inválida")

        self.__seguroPorDia = float(novo_seguro)

    def get_seguro(self) -> float:
        return self.__seguroPorDia

    def set_disponivel(self, novo_disponivel: bool) -> None:
        try:
            novo_disponivel = bool(novo_disponivel)
        except ValueError:
            raise ValueError("Valor inválido para disponível")

        self.__disponivel = novo_disponivel

    def is_disponivel(self) -> bool:
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
        diaria: float = None,
        seguro: float = None,
        disponivel: bool = None,
        vazio: bool = False
    ) -> None:
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
        if not type(valor) is str:
            raise TypeError("Tipo inválido")
        novo_valor = valor.replace(',', '.')
        if not novo_valor.isnumeric():
            raise ValueError("Valor inválido")
        return float(novo_valor)

    def is_valido(self) -> bool:
        if (
                self.get_id() is None
                or self.get_modelo() is None
                or self.get_cor() is None
                or self.get_ano() is None
                or self.get_placa() is None
                or self.get_cambio() is None
                or self.get_diaria() is None
                or self.get_seguro() is None
                or self.is_disponivel() is None
        ):
            return False
        return True

    def get_linha(self) -> tuple:
        return (
            self.get_id(),
            self.get_modelo(),
            self.get_cor(),
            self.get_ano(),
            self.get_placa(),
            self.get_cambio(),
            self.get_diaria(),
            self.get_seguro(),
            "Sim" if self.is_disponivel() else "Não"
        )
