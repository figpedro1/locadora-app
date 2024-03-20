import csv
import os

from Carro import *


class Carros:
    __lista: list[Carro] = []
    __salvo = False
    __caminho_para_arquivo = None
    novo_carro = Carro(vazio=True)

    def __init__(self, caminho_para_arquivo):
        diretorio, arquivo = os.path.split(caminho_para_arquivo)
        if not os.path.isdir(diretorio):
            os.makedirs(diretorio)
            if not os.path.isdir(diretorio):
                raise ValueError("Caminho inválido")

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
                            int(linha[9]),
                            bool(linha[10] == "Sim")
                        )
                    )
        except FileNotFoundError:
            with open(caminho_para_arquivo, 'w', newline="") as arquivo:
                escritor = csv.writer(arquivo)
                Carro()
                escritor.writerow([
                    "Identificação do carro",
                    "Modelo",
                    "Cor",
                    "Ano de fabricação",
                    "Placa",
                    "Cambio",
                    "Categoria",
                    "Quilometragem",
                    "Valor da diária",
                    "Valor do seguro por dia",
                    "Disponível"])
        self.__salvo = True

    def add_carro(self):
        if not self.novo_carro.is_valido():
            raise ValueError("Declare todos os atributos do novo carro antes de adicioná-lo")
        self.__lista.append(self.novo_carro)
        self.novo_carro = Carro(vazio=True)
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

    def modificar_carro(
            self,
            veiculo_id: int,
            modelo: str | None = None,
            cor: str | None = None,
            ano: int | None = None,
            placa: str | None = None,
            cambio: str | None = None,
            categoria: str | None = None,
            quilometragem: int | None = None,
            diaria: float | None = None,
            seguro: float | None = None,
            disponivel: bool | str | None = None
    ):
        if veiculo_id > len(self.__lista):
            raise Exception("Id de veículo inexistente")
        if modelo is not None:
            self.__lista[veiculo_id].set_modelo(modelo)
        if cor is not None:
            self.__lista[veiculo_id].set_cor(cor)
        if ano is not None:
            self.__lista[veiculo_id].set_ano(ano)
        if placa is not None:
            self.__lista[veiculo_id].set_placa(placa)
        if cambio is not None:
            self.__lista[veiculo_id].set_cambio(cambio)
        if categoria is not None:
            self.__lista[veiculo_id].set_categoria(categoria)
        if quilometragem is not None:
            self.__lista[veiculo_id].set_quilometragem(quilometragem)
        if diaria is not None:
            self.__lista[veiculo_id].set_diaria(diaria)
        if seguro is not None:
            self.__lista[veiculo_id].set_seguro(seguro)
        if disponivel is not None:
            if type(disponivel) is str:
                self.__lista[veiculo_id].set_disponivel(disponivel.upper == "SIM")
            else:
                self.__lista[veiculo_id].set_disponivel(disponivel)
        self.__salvo = False

    def is_salvo(self):
        return self.__salvo
