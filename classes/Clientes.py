import csv
import os

from Cliente import *


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
    novo_cliente: Cliente = Cliente(vazio=True)

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
        """
        Adiciona o Cliente "novo_cliente" a lista de clientes e gera um novo cliente vazio em "novo_cliente"
        :return: None
        :rtype: None
        :raises Exception: Se o cliente não for válido será gerado um erro
        """
        if not self.novo_cliente.is_valido():
            raise Exception("Informações faltando no novo cliente")
        self.__lista[self.novo_cliente.get_cpf()] = self.novo_cliente
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

    def is_salvo(self) -> bool:
        """
        Verifica se a lista está sincronizada com o arquivo CSV
        :return: True se estiver sincronizada, False caso contrário
        :rtype: bool
        """
        return self.__salvo
