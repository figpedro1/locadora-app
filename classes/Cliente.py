class Cliente:
    __cpf: str | None = None
    __nome: str | None = None
    __idade: int | None = None
    __endereco: str | None = None
    __cidade: str | None = None
    __estado: str | None = None

    def set_cpf(self, novo_cpf: str) -> None:
        novo_cpf = str(novo_cpf).replace(".", "").replace("-", "")
        if len(novo_cpf) != 11 or (not novo_cpf.isnumeric()):
            raise ValueError("CPF inválido.")
        if not novo_cpf.isnumeric():
            raise ValueError("CPF inválido")

        resto_primeira = (
            (
                int(novo_cpf[0]) * 10 +
                int(novo_cpf[1]) * 9 +
                int(novo_cpf[2]) * 8 +
                int(novo_cpf[3]) * 7 +
                int(novo_cpf[4]) * 6 +
                int(novo_cpf[5]) * 5 +
                int(novo_cpf[6]) * 4 +
                int(novo_cpf[7]) * 3 +
                int(novo_cpf[8]) * 2
            ) % 11
        )

        resto_segunda = (
            (
                    int(novo_cpf[0]) * 11 +
                    int(novo_cpf[1]) * 10 +
                    int(novo_cpf[2]) * 9 +
                    int(novo_cpf[3]) * 8 +
                    int(novo_cpf[4]) * 7 +
                    int(novo_cpf[5]) * 6 +
                    int(novo_cpf[6]) * 5 +
                    int(novo_cpf[7]) * 4 +
                    int(novo_cpf[8]) * 3 +
                    int(novo_cpf[9]) * 2
            ) % 11
        )

        if (
            (resto_primeira <= 1 and int(novo_cpf[9]) != 0) or
            (resto_segunda <= 1 and int(novo_cpf[10]) != 0)
        ):
            raise ValueError("CPF inválido")
        if (
            (resto_primeira > 1 and 11 - resto_primeira != int(novo_cpf[9])) or
            (resto_segunda > 1 and 11 - resto_segunda != (novo_cpf[10]))
        ):
            raise ValueError("CPF inválido")

        self.__cpf = "{}.{}.{}-{}".format(novo_cpf[:3], novo_cpf[3:6], novo_cpf[6:9], novo_cpf[9:])

    def get_cpf(self) -> str:
        return self.__cpf

    def set_nome(self, novo_nome: str) -> None:
        self.__nome = str(novo_nome)

    def get_nome(self) -> str:
        return self.__nome

    def set_idade(self, nova_idade: int) -> None:
        nova_idade = int(nova_idade)
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa")
        self.__idade = nova_idade

    def get_idade(self):
        return self.__idade

    def set_endereco(self, novo_endereco: str) -> None:
        self.__endereco = str(novo_endereco)

    def get_endereco(self) -> str:
        return self.__endereco

    def set_cidade(self, nova_cidade: str) -> None:
        self.__cidade = str(nova_cidade)

    def get_cidade(self) -> str:
        return self.__cidade

    def set_estado(self, novo_estado: str) -> None:
        self.__estado = str(novo_estado)

    def get_estado(self) -> str:
        return self.__estado
