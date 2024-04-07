from Clientes import *
import csv
from datetime import *

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

    @staticmethod
    def formata_data(data: str | dict) -> dict:
        """
        Transforma uma string em um dicionário com os campos 'dia', 'mês', 'ano', 'hora' ou atribui um dicionário com esses campos a um novo dicionário.

        :param data: Uma data qualquer no formata XX/XX/XXXX XX:XX
        :type data: str | dict
        :return: Retorna a data no formato de um dicionário com os campos 'dia', 'mês', 'ano', 'hora'
        :rtype: dict
        """
        if type(data) != str and type(data) != dict:
            raise TypeError("A data pode ser somente uma string ou um dicionário")
        if type(data) == str:
            if data == "":
                raise ValueError("A data não pode ser uma string vazia")
            else:
                nova_data = {}
                nova_data['dia'] = data.split('/')[0]
                nova_data['mes'] = data.split('/')[1]
                ano = str(data.split(' ')[0])
                nova_data['ano'] = ano.split('/')[2]
                nova_data['hora'] = data.split(' ')[1]
                return nova_data
        else:
            nova_data = {}
            nova_data['dia'] = data['dia']
            nova_data['mes'] = data['mes']
            nova_data['ano'] = data['ano']
            nova_data['hora'] = data['hora']
            return nova_data

    def __init__(self, 
                 id_locacao: int = 0,
                 id_carro: int = None,
                 cpf_cliente: str | None =None,      
                 data_locacao: str = datetime.now().strftime('%d/%m/%Y %H:%M'),
                 data_devolucao: str = "00/00/00 00:00",
                 km_inicial: int = 0,
                 km_final: int = 0,
                 seguro: str = None,
                 valor_total: float = 0,
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
        self.__data_locacao = {}
        self.__data_locacao = self.formata_data(data_locacao)
        
    def get_data_locacao(self) -> dict:
        return self.__data_locacao
    
    def set_data_devolucao(self, data_devolucao: dict | str) -> None:
        self.__data_devolucao = {}
        self.__data_devolucao = self.formata_data(data_devolucao)

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

    @staticmethod
    def calcula_valor(valor_diaria: float = None, 
                      valor_seguro: float = 0, 
                      data_locacao: str | dict = None, 
                      data_devolucao: str | dict = datetime.now().strftime('%d/%m/%Y %H:%M')) -> float:
       
        if valor_diaria < 0:
            raise ValueError("O valor da diária não pode ser negativo")
        
        if valor_seguro < 0:
            raise ValueError("O valor do seguro não pode ser negativo")
        
        if (type(data_locacao) != str and type(data_locacao) != dict) or (type(data_devolucao) != str and type(data_devolucao)!= dict):
            raise TypeError("As datas precisam ser do tipo string ou dicionário")
        
        if type(data_locacao) == dict:
            data_loc = str(data_locacao['dia'])+'/'+str(data_locacao['mes'])+'/'+str(data_locacao['ano'])+' '+str(data_locacao['hora'])
        else:
            data_loc = data_locacao
        
        if type(data_devolucao) == dict:
            data_devol = str(data_devolucao['dia'])+'/'+str(data_devolucao['mes'])+'/'+str(data_devolucao['ano'])+' '+str(data_devolucao['hora'])
        else:
            data_devol = data_devolucao
        data_loc = datetime.strptime(data_loc, '%d/%m/%Y %H:%S')
        data_devol = datetime.strptime(data_devol, '%d/%m/%Y %H:%S')
        dias = (data_devol - data_loc).days
        if dias <= 0:
            raise ValueError("Não é possível calcular a diaria total para uma locação de menos de 24 horas")
        lixo = str(data_devol - data_loc).split(" ")
        horas = int(lixo[2].split(':')[0])
        return (valor_diaria*dias)+((horas/24)*valor_diaria)+valor_seguro
    
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
        except OSError:
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
        self.atualiza_arquivo()
    
    def tam(self) -> int:
        return len(self.__lista)
    
    def id_locacoes(self)->int:
        if self.__lista == []:
            return 0
        else:
            tamanho = self.tam()
            return int(self.__lista[tamanho-1]['IdLocacao']) + 1
        
    def seguro(self, id_locacao: int)->str:
        if id_locacao < 0:
            raise ValueError('Id inválido')
        i = 0
        while i < self.tam() and int(self.__lista[i]['IdLocacao']) != id_locacao:
            i += 1
        if i == self.tam():
            raise ValueError("Esse Id não existe")
        else:
            return str(self.__lista[i]['Seguro'])
        
    def altera_locacao(self, 
                       id_locacao: int = None, 
                       data_devolucao: str | dict = datetime.now().strftime('%d/%m/%Y %H:%M'), 
                       km_final: int = None,
                       valor_total: float = None) -> None:
        i = 0
        while i < self.tam() and int(self.__lista[i]['IdLocacao']) != id_locacao:
            i += 1
        if i == self.tam():
            raise ValueError("Esse Id não existe")
        if int(km_final) < 0 or km_final < int(self.__lista[i]['KmInicial']):
            raise ValueError("A Quilometragem não pode ser negativa ou menor do que a quilometragem inicial")
        if type(data_devolucao) != str and type(data_devolucao) != dict:
            raise TypeError("A data de devolução pode ser somente do tipo string ou do tipo dicionário")
        if valor_total < 0:
            raise ValueError("O valor total não pode ser negativo")
        nova_data={}
        nova_data = Locacao.formata_data(data_devolucao)
        self.__lista[i]['DataDevolucao'] = str(nova_data['dia'])+'/'+str(nova_data['mes'])+'/'+str(nova_data['ano'])+' '+str(nova_data['hora'])
        self.__lista[i]['KmFinal'] = int(km_final)
        self.__lista[i]['ValorTotal'] = "{:.2f}".format(float(valor_total))
        self.atualiza_arquivo()
