from Clientes import *
from Carros import *
import csv
from datetime import datetime

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
    __data_locacao: dict | str | None = datetime.now().strftime('%d/%m/%Y %H:%M')
    __data_devolucao: dict | str | None = "00/00/00 00:00"
    __km_inicial: int | None = 0
    __km_final: int | None = 0
    __seguro: str | None = None
    __valor_total: float = 0

    def __init__(self, 
                 id_locacao: int = 0,
                 id_carro: int = None,
                 cpf_cliente: str | None =None,      
                 data_locacao: str = datetime.now().strftime('%d/%m/%Y %H:%M'),
                 data_devolucao: str = "00/00/00 00:00",
                 km_inicial: int = 0,
                 km_final: int = 0,
                 seguro: str = None,
                 valor_total: float = None,
                 vazio: bool = False
                 ) -> None:
        """
        Inicializador da classe "Locacao".
        
        :param id_locacao: ID de uma nova locação.
        :type id_locacao: int | None
        :param id_carro: ID do carro escolhido.
        :type id_carro: int | None
        :param cpf_cliente: CPF do cliente que está realizando a locação.
        :type cpf_cliente: str | None
        :param data_locacao: Data da locação, por padrão é o dia atual.
        :type data_locacao: dict | str | None
        :param data_devolucao: Data da devolução, por padrão é 00/00/00.
        :type data_devolucao: dict | str | None
        :param km_inicial: Quilometragem do carro locado no dia da locação, por padrão, o valor é 0.
        :type km_inicial: int | None
        :param km_final: Quilometragem do carro locado no dia da devolução, por padrão, o valor é 0.
        :type km_final: int | None
        :param seguro: "Sim", "Não", "Nao". Não precisa ser escrito necessariamente dessa forma.
        :type seguro: str | None
        :param valor_total: Valor total da locação.
        :type valor_total: float | None
        :return: None
        """
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
    def set_id_locacao(self, novo_id) -> None:
        """
        Atribui um novo valor de ID da locação. 
        Sendo que esse valor não poderá ser menor que 0.
        
        :param novo_id: Novo id de locação
        :return: None
        :raises ValueError: Caso o valor seja menor que 0
        """
        if novo_id < 0:
            raise ValueError("O Id não pode ser menor que 0")
        self.__id_locacao = int(novo_id)
    
    def get_id_locacao(self) -> int:
        """
        Retorna o valor do id da locação.
        :return: Valor do id locação.
        :rtype: int
        """
        return self.__id_locacao

    #Set e Get do id do carro
    def set_id_carro(self, id_carro: int) -> None:
        """
        Atribui um novo ID do carro locado.
        Sendo que esse valor não poderá ser menor que 0.

        :param id_carro: Id do carro locado.
        :return: None
        :raises ValueError: Caso o valor seja menor que 0.
        """
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
                self.__data_locacao = {}
                self.__data_locacao['dia'] = data_locacao.split('/')[0]
                self.__data_locacao['mes'] = data_locacao.split('/')[1]
                ano = str(data_locacao.split(' ')[0])
                self.__data_locacao['ano'] = ano.split('/')[2]
                self.__data_locacao['hora'] = str(data_locacao.split(' ')[1])

            else:
                raise ValueError("A data não pode ser uma string vazia")
        elif type(data_locacao) == dict:
            self.__data_locacao = {}
            self.__data_locacao['dia'] = data_locacao['dia']
            self.__data_locacao['mes'] = data_locacao['mes']
            self.__data_locacao['ano'] = data_locacao['ano']
            self.__data_locacao['hora'] = data_locacao['hora']
        else:
            raise TypeError("A data precisa ser uma string XX/XX/XXXX XX:XX ou um dicionário")
        
    def get_data_locacao(self) -> dict:
        return self.__data_locacao
    
    def set_data_devolucao(self, data_devolucao: dict | str) -> None:
        if type(data_devolucao) == str:
            if data_devolucao != "":
                self.__data_devolucao = {}
                self.__data_devolucao['dia'] = data_devolucao.split('/')[0]
                self.__data_devolucao['mes'] = data_devolucao.split('/')[1]
                ano = str(data_devolucao.split(' ')[0])
                self.__data_devolucao['ano'] = ano.split('/')[2]
                self.__data_devolucao['hora'] = str(data_devolucao.split(' ')[1])
            else:
                raise ValueError("A data não pode ser uma string vazia")
        elif type(data_devolucao) == dict:
            self.__data_devolucao = {}
            self.__data_devolucao['dia'] = data_devolucao['dia']
            self.__data_devolucao['mes'] = data_devolucao['mes']
            self.__data_devolucao['ano'] = data_devolucao['ano']
            self.__data_devolucao['hora'] = data_devolucao['hora']
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
    
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#Início classe Locações
class Locacoes:
    __lista: list = []

    def __init__(self, nome_arquivo="Locacoes.csv") -> None:
        try:
            self.__lista = []
            arquivo_locacoes = open(nome_arquivo, "r", newline="")
            campos = csv.DictReader(arquivo_locacoes, delimiter=';')
            for linhas in campos:
                locacoes = {}
                locacoes['IdLocacao'] = linhas['IdLocacao']
                locacoes['IdCarro'] = linhas['IdCarro']
                locacoes['CPF'] = linhas['CPF']
                locacoes['DataLocacao'] = linhas['DataLocacao']
                locacoes['DataDevolucao'] = linhas['DataDevolucao']
                locacoes['KmInicial'] = linhas['KmInicial']
                locacoes['KmFinal'] = linhas['KmFinal']
                locacoes['Seguro'] = linhas['Seguro']
                locacoes['ValorTotal'] = linhas['ValorTotal']
                self.__lista.append(locacoes)
            arquivo_locacoes.close()
        except FileNotFoundError:
            arquivo_locacoes = open(nome_arquivo, "a", newline="")
            campos = csv.writer(arquivo_locacoes, delimiter=';')
            campos.writerow((
                "IdLocacao",
                "IdCarro",
                "CPF",
                "DataLocacao",
                "DataDevolucao",
                "KmInicial",
                "KmFinal",
                "Seguro",
                "ValorTotal"
            ))
            arquivo_locacoes.close()

    def get_lista(self) -> dict:
        return self.__lista
    

    def atualiza_arquivo(self) -> None:   
        nome_arquivo = "Locacoes.csv"
        try:
            arquivo = open(nome_arquivo, "w", newline="")
            campos = ["IdLocacao",
                "IdCarro",
                "CPF",
                "DataLocacao",
                "DataDevolucao",
                "KmInicial",
                "KmFinal",
                "Seguro",
                "ValorTotal"
            ]
            manipulador = csv.DictWriter(arquivo, fieldnames=campos, delimiter=';')
            manipulador.writeheader()
            manipulador.writerows(self.__lista)
            arquivo.close()
        except OSError as err:
            raise OSError("Não foi possível abrir o arquivo")
    
    def add_locacao(self, nova_locacao: Locacao) -> None:
        locacao = {}
        locacao['IdLocacao'] = nova_locacao.get_id_locacao()
        locacao['IdCarro'] = nova_locacao.get_id_carro()
        locacao['CPF'] = nova_locacao.get_cpf_cliente()
        locacao['DataLocacao'] = str(nova_locacao.get_data_locacao()['dia'])+'/'+str(nova_locacao.get_data_locacao()['mes'])+'/'+str(nova_locacao.get_data_locacao()['ano'])+' '+str(nova_locacao.get_data_locacao()['hora']) 
        locacao['DataDevolucao'] = str(nova_locacao.get_data_devolucao()['dia'])+'/'+str(nova_locacao.get_data_devolucao()['mes'])+'/'+str(nova_locacao.get_data_devolucao()['ano'])+' '+str(nova_locacao.get_data_devolucao()['hora']) 
        locacao['KmInicial'] = nova_locacao.get_km_inicial()
        locacao['KmFinal'] = nova_locacao.get_km_final()
        locacao['Seguro'] = nova_locacao.get_seguro()
        locacao['ValorTotal'] = nova_locacao.get_valor_total()
        self.__lista.append(locacao)
    
    def tam(self) -> int:
        return len(self.__lista)
    
    def id_locacoes(self)->int:
        if self.__lista == []:
            return 0
        else:
            tamanho = self.tam()
            return int(self.__lista[tamanho-1]['IdLocacao']) + 1

#Testando a funcionalidade das classes e outros
teste = Locacoes()
locaca = Locacao(teste.id_locacoes(), 0, "000.000.000-00", seguro="Sim", valor_total=0, data_devolucao="00/00/00 00:00")
teste.add_locacao(locaca)
teste.atualiza_arquivo()