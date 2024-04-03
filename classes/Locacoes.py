from Clientes import *
from Carros import *
import csv

class Locacao:
    """
    Classe para iniciar uma nova locação.
    Todos os atributos são privados, como denota o prefixo "__".
    Set's são utilizados para atribuir valores aos atributos,
    Get's são utilizados para devolver os valores dos atributos.

    Atributos
    ---------------
        __id_locacao: int = id da locação 
        __id_carro: int = id do carro que foi locado
        __cpf_cliente: str = cpf do cliente
        __data_locacao: dict = data do início da locação
        __data_devolucao: dict = data da devolução do carro
        __km_inicial: int = quilometragem do carro antes da locação
        __km_final: int = quilometragem do carro depois da locação
        __seguro: str = se o cliente deseja obter seguro ou não
        __valor_total: float = valor total da locação
    """
    

    __id_locacao: int | None = 0
    __id_carro: int | None = None
    __cpf_cliente: str | None = None
    __data_locacao: dict = None
    __data_devolucao: dict | None = None
    __km_inicial: int | None = 0
    __km_final: int | None = 0
    __seguro: str | None = "Não"
    __valor_total: float = 0

    def __init__(self, 
                 id_locacao: int = None,
                 id_carro: int = None,
                 cpf_cliente: str | None =None,      
                 data_locacao: dict = None,
                 data_devolucao: dict = None,
                 km_inicial: int = 0,
                 km_final: int = 0,
                 seguro: str = None,
                 valor_total: float = None,
                 vazio: bool = False
                 ) -> None:
        if not vazio:
            self.set_id_locacao(id_locacao)
            self.set_id_carro(id_carro)
            self.set_cpf_cliente(cpf_cliente)
            self.set_data_locacao(data_locacao)
            self.set_data_devolucao(data_devolucao)
            self.set_km_inicial(km_inicial)
            self.set_km_final(km_final)
            self.set_seguro(seguro)
            self.set_valor_total(valor_total)


    #Set e Get do id da Locação
    def set_id_locacao(self, novo_id_locacao: int) -> None:
        novo_id_locacao = int(novo_id_locacao)
        if novo_id_locacao < 0:
            raise ValueError("Id não pode ser negativo")
        self.__idLocacao = novo_id_locacao
    
    def get_id_locacao(self) -> int:
        return self.__idLocacao

    def set_id_carro(self, id_carro: int) -> None:
        if id_carro < 0:
            raise ValueError("Id não pode ser negaivo")
        self.__id_carro = id_carro
    
    def get_id_carro(self) -> int:
        return self.__id_carro

    #Set e Get do CPF do cliente
    def set_cpf_cliente(self, novoCpf: str) -> None:
        """
        Atribui o CPF do cliente na classe Locações
        """
        self.__cpf_cliente = Cliente.formatar_cpf(novoCpf)

    def get_cpf_cliente(self) -> str:
        return self.__cpf_cliente
    
    def set_data_locacao(self, data_locacao: dict | str) -> None:
        if type(data_locacao) == str:
            if data_locacao != "":
                nova_data = data_locacao.split(sep="/;")
                self.__data_locacao['dia'] = int(nova_data[0])
                self.__data_locacao['mes'] = int(nova_data[1])
                self.__data_locacao['ano'] = int(nova_data[2])
                self.__data_locacao['hora'] = int(nova_data[3])
            else:
                raise ValueError("A data não pode ser uma string vazia")
        elif type(data_locacao) == dict:
            self.__data_locacao['dia'] = int(data_locacao['dia'])
            self.__data_locacao['mes'] = int(data_locacao['mes'])
            self.__data_locacao['ano'] = int(data_locacao['ano'])
            self.__data_locacao['hora'] = int(data_locacao['hora'])
        else:
            raise TypeError("A data precisa ser uma string XX/XX/XXXX XX:XX ou um dicionário")
        
    def get_data_locacao(self) -> dict:
        return self.__data_locacao
    
    def set_data_devolucao(self, data_devolucao: dict | str) -> None:
        if type(data_devolucao) == str:
            if data_devolucao != "":
                nova_data = data_devolucao.split("/;")
                self.__data_devolucao['dia'] = int(nova_data[0])
                self.__data_devolucao['mes'] = int(nova_data[1])
                self.__data_devolucao['ano'] = int(nova_data[2])
                self.__data_devolucao['hora'] = int(nova_data[3])
            else:
                raise ValueError("A data não pode ser uma string vazia")
        elif type(data_devolucao) == dict:
            self.__data_devolucao['dia'] = int(data_devolucao['dia'])
            self.__data_devolucao['mes'] = int(data_devolucao['mes'])
            self.__data_devolucao['ano'] = int(data_devolucao['ano'])
            self.__data_devolucao['hora'] = int(data_devolucao['hora'])
        else:
            raise TypeError("A data precisa ser uma string XX/XX/XXXX XX:XX ou um dicionário")

    def get_data_devolucao(self) -> dict:
        return self.__data_devolucao


    def set_km_inicial(self, km_inicial: int) -> None:
        km_inicial = int(km_inicial)
        if km_inicial < 0:
            raise ValueError("A quilometragem não pode ser inferior a 0")
        self.__km_inicial = km_inicial

    def get_km_inicial(self) -> int:
        return self.__km_inicial
    
    def set_km_final(self, km_final: int) -> None:
        km_final = int(km_final)
        if km_final < 0:
            raise ValueError("A quilometragem não pode ser inferior a 0")
        if km_final < self.__km_inicial:
            raise ValueError("A quilometragem final não pode ser inferior a quilometragem inicial")
        self.__km_final = km_final

    def get_km_final(self) -> int:
        return self.__km_final
    
    def set_seguro(self, seguro: str) -> None:
        if seguro.upper() not in ("SIM", "NÃO", "NAO"):
            raise ValueError("O seguro precisa ser sim ou não")
        if seguro.upper() == "NAO":
            seguro = "Não"
        self.__seguro = seguro.capitalize()

    def get_seguro(self) -> str:
        return self.__seguro
    
    def set_valor_total(self, valor_total: float) -> None:
        valor_total = float(valor_total)
        if valor_total < 0:
            raise ValueError("O valor total não pode ser negativo")
        self.__valor_total = valor_total
    
    def get_valor_total(self) -> float:
        return self.__valor_total


class Locacoes:
    __lista: list = []
    __nome_arquivo: str = None

    def __init__(self, nome_arquivo="Locacoes.csv") -> None:
        try:
            self.__lista = []
            arquivo_locacoes = open(nome_arquivo, "r", newline="")
            campos = csv.DictReader(arquivo_locacoes, delimiter=';')
            for linhas in campos:
                locacoes = {}
                locacoes['idLoc'] = linhas['Id Locacao']
                locacoes['idCarro'] = linhas['Id Carro']
                locacoes['cpf'] = linhas['CPF']
                locacoes['dataLoc'] = linhas['Data Locacao']
                locacoes['dataDevol'] = linhas['Data Devolucao']
                locacoes['kmI'] = linhas['Km Inicial']
                locacoes['kmF'] = linhas['Km Final']
                locacoes['seguro'] = linhas['Seguro']
                locacoes['valorT'] = linhas['Valor Total']
                self.__lista.append(locacoes)
            arquivo_locacoes.close()
        except FileNotFoundError:
            arquivo_locacoes = open(nome_arquivo, "a", newline="")
            campos = csv.writer(arquivo_locacoes, delimiter=';')
            campos.writerow((
                "Id Locacao",
                "Id Carro",
                "CPF",
                "Data Locacao",
                "Data Devolucao",
                "Km Inicial",
                "Km Final",
                "Seguro",
                "Valor Total"
            ))
            arquivo_locacoes.close()

    def get_lista(self) -> dict:
        return self.__lista
    
    def add_locacao(self, nova_locacao: Locacao) -> None:
        locacao = {}
        locacao['idLoc'] = nova_locacao.get_id_locacao()
        locacao['idCarro'] = nova_locacao.get_id_carro()
        locacao['cpf'] = nova_locacao.get_cpf_cliente()
        locacao['dataLoc'] = nova_locacao.get_data_locacao()
        locacao['dataDevol'] = nova_locacao.get_data_devolucao()
        locacao['kmInicial'] = nova_locacao.get_km_inicial()
        locacao['kmFinal'] = nova_locacao.get_km_final()
        locacao['seguro'] = nova_locacao.get_seguro()
        locacao['valorT'] = nova_locacao.get_valor_total()
        self.__lista.append(locacao)

teste = Locacoes()
print(teste.get_lista())
        