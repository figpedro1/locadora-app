import csv

from Carro import *


class Carros:
    lista = []
    __salvo = True
    novo_carro = Carro(vazio=True)

    def __init__(self, nome_arquivo):
        with open(nome_arquivo, 'r', newline="") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=";")
            next(arquivo_csv, None)

            for linha in arquivo_csv:
                self.lista.append(
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
                        int(linha[9]),
                        bool(linha[10])
                    )
                )

    def add_carro(self):
        if not self.novo_carro.is_valido():
            raise ValueError("Declare todos os atributos do novo carro antes de adicioná-lo")
        self.lista.append(self.novo_carro)
        self.novo_carro = Carro(vazio=True)
        self.__salvo = False

    def salvar_csv(self, nome_arquivo):
        if self.__salvo:
            return

        with open(nome_arquivo, 'w', newline="") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            lista_linha = (
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
            escritor.writerow(lista_linha)

            for linha in self.lista:
                lista_linha = []
                for coluna in linha:
                    lista_linha.append(coluna)
                escritor.writerow(lista_linha)
            self.__salvo = True
