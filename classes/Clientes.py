import csv
import os

from Cliente import *


class Clientes:
    __lista: dict[str, Cliente] = {}
    __salvo: bool = False
    __caminho_para_arquivo: str | None = None
    novo_cliente: Cliente = Cliente(vazio=True)

    def __init__(self, caminho_para_arquivo: str) -> None:
        diretorio, arquivo = os.path.split(caminho_para_arquivo)
        if not os.path.isdir(diretorio):
            os.makedirs(diretorio)
            if not os.path.isdir(arquivo):
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
                                                linha[5]
                                            )

        except FileNotFoundError:
            with open(self.__caminho_para_arquivo, "w", newline="") as arquivo:
                escritor = csv.writer(arquivo, delimiter=";")
                escritor.writerow(["CPF", "Nome", "Idade", "Endereço", "Cidade", "Estado"])

        self.__salvo = True

    def salvar_csv(self) -> None:
        if self.__salvo:
            return

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

    def add_cliente(self) -> None:
        if not self.novo_cliente.is_valido():
            raise Exception("Informações faltando no novo cliente")
        self.__lista[self.novo_cliente.get_cpf()] = self.novo_cliente
        self.__salvo = False

    def modificar_cliente(
            self,
            cpf: str,
            nome: str | None = None,
            idade: int | None = None,
            endereco: str | None = None,
            cidade: str | None = None,
            estado: str | None = None
    ) -> None:
        cpf = Cliente.formatar_cpf(cpf)
        if cpf not in self.__lista:
            raise Exception("Cliente não cadastrado")
        if nome is not None:
            self.__lista[cpf].set_nome(nome)
        if idade is not None:
            self.__lista[cpf].set_idade(idade)
        if endereco is not None:
            self.__lista[cpf].set_endereco(endereco)
        if cidade is not None:
            self.__lista[cpf].set_cidade(cidade)
        if estado is not None:
            self.__lista[cpf].set_estado(estado)
        self.__salvo = False

    def is_salvo(self) -> bool:
        return self.__salvo
