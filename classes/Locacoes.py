from classes.Clientes import *
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
    __seguro: bool | None = None
    __valor_total: float = 0

    @staticmethod
    def formata_data(data: str | dict) -> dict:
        """
        Transforma uma string em um dicionário com os campos 'dia', 'mês', 'ano', 'hora' ou atribui um dicionário com
        esses campos a um novo dicionário.

        :param data: Uma data qualquer no formato XX/XX/XXXX XX:XX
        :type data: str | dict
        :return: Retorna a data no formato de um dicionário com os campos 'dia', 'mês', 'ano', 'hora'
        :rtype: dict
        :raises ValueError: Quando a string não é válida
        """
        if type(data) is dict:
            return data
        if type(data) is not str:
            raise TypeError("Data deve ser uma string ou um dicionário")

        data_dict = datetime.strptime(data, '%d/%m/%Y %H:%M')

        data = {
            'dia': str(data_dict.day),
            'mes': str(data_dict.month),
            'ano': str(data_dict.year),
            'hora': (str(data_dict.hour) + str(data_dict.minute))
        }

        return data

    def __init__(self, 
                 id_locacao: int = 0,
                 id_carro: int = None,
                 cpf_cliente: str | None = None,
                 data_locacao: str = datetime.now().strftime('%d/%m/%Y %H:%M'),
                 data_devolucao: str = "00/00/00 00:00",
                 km_inicial: int = 0,
                 km_final: int = 0,
                 seguro: bool = None,
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

    # Set e Get do id da Locação
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

    # Set e Get do id do carro
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

    # Set e Get do CPF do cliente
    def set_cpf_cliente(self, novo_cpf: str) -> None:
        """
        Atribui o CPF do cliente na classe Locações
        """
        self.__cpf_cliente = Cliente.formatar_cpf(novo_cpf)

    def get_cpf_cliente(self) -> str:
        return self.__cpf_cliente
    
    def set_data_locacao(self, data_locacao: dict | str) -> None:
        self.__data_locacao = data_locacao
        
    def get_data_locacao(self) -> dict:
        return self.__data_locacao
    
    def set_data_devolucao(self, data_devolucao: dict | str) -> None:
        self.__data_devolucao = data_devolucao

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
        self.__km_final = km_final

    def get_km_final(self) -> int:
        return self.__km_final
    
    def set_seguro(self, seguro: str | bool) -> None:
        seguro = str(seguro)
        if seguro.upper() not in ("SIM", "NÃO", "NAO", "TRUE", "FALSE"):
            raise ValueError("Os valores válidos para seguro são 'Sim' e 'Não'")
        self.__seguro = seguro.upper() == "SIM" or seguro.upper() == "TRUE"

    def get_seguro(self) -> bool:
        return self.__seguro
    
    def set_valor_total(self, valor_total: float) -> None:
        valor_total = float(valor_total)
        if valor_total < 0:
            raise ValueError("O valor total não pode ser negativo")
        self.__valor_total = valor_total
    
    def get_valor_total(self) -> float:
        return self.__valor_total

    def get_linha(self) -> tuple:
        return (
            str(self.get_id_locacao()),
            str(self.get_id_carro()),
            str(self.get_cpf_cliente()),
            str(self.get_data_locacao()),
            str(self.get_data_devolucao()),
            str(self.get_km_inicial()),
            str(self.get_km_final()),
            "Sim" if str(self.get_seguro()) else "Não",
            str(self.get_valor_total()),
        )


# Início classe Locações
class Locacoes:
    __lista: list = []
    __caminho_arquivo: str

    @staticmethod
    def calcula_valor(valor_diaria: float = None, 
                      valor_seguro: float = 0, 
                      data_locacao: str | dict = None, 
                      data_devolucao: str | dict = datetime.now().strftime('%d/%m/%Y %H:%M')) -> float:
       
        if valor_diaria < 0:
            raise ValueError("O valor da diária não pode ser negativo")
        
        if valor_seguro < 0:
            raise ValueError("O valor do seguro não pode ser negativo")
        
        if (
            (type(data_locacao) is not str and type(data_locacao) is not dict) or
            (type(data_devolucao) is not str and type(data_devolucao) is not dict)
        ):
            raise TypeError("As datas precisam ser do tipo string ou dicionário")
        
        if type(data_locacao) is dict:
            data_loc = (
                    str(data_locacao['dia']) + '/' +
                    str(data_locacao['mes']) + '/' +
                    str(data_locacao['ano']) + ' ' +
                    str(data_locacao['hora'])
            )
        else:
            data_loc = data_locacao
        
        if type(data_devolucao) is dict:
            data_devol = (str(data_devolucao['dia'])+'/'+str(data_devolucao['mes'])+'/'+str(data_devolucao['ano']) +
                          ' '+str(data_devolucao['hora']))
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

    def __init__(self, caminho_arquivo="planilhas/Locacoes.csv") -> None:
        self.__lista = []
        try:
            with open(caminho_arquivo, "r", newline="") as arquivo_locacoes:
                arquivo_csv = csv.reader(arquivo_locacoes, delimiter=';')
                next(arquivo_csv, None)

                for linhas in arquivo_csv:
                    locacao = Locacao(
                        int(linhas[0]),
                        int(linhas[1]),
                        linhas[2],
                        linhas[3],
                        linhas[4],
                        int(linhas[5]),
                        int(linhas[6]),
                        linhas[7].upper() == "SIM",
                        float(linhas[8])
                    )

                    self.__lista.append(locacao)
        except FileNotFoundError:
            with open(caminho_arquivo, "w", newline="") as arquivo_locacoes:
                escritor = csv.writer(arquivo_locacoes, delimiter=';')
                escritor.writerow((
                    "Id da locacao",
                    "Id do carro",
                    "CPF do cliente",
                    "Data de locação",
                    "Data de devolução",
                    "Quilometragem inicial",
                    "Quilometragem final",
                    "Optou por seguro",
                    "Valor total"
                ))
        self.__caminho_arquivo = caminho_arquivo

    def get_locacao(self, id_locacao: int) -> Locacao:
        return self.__lista[id_locacao]

    def salvar_csv(self):
        with open(self.__caminho_arquivo, 'w', newline="") as arquivo_locacoes:
            escritor = csv.writer(arquivo_locacoes, delimiter=';')
            escritor.writerow((
                "Id da locacao",
                "Id do carro",
                "CPF do cliente",
                "Data de locação",
                "Data de devolução",
                "Quilometragem inicial",
                "Quilometragem final",
                "Optou por seguro",
                "Valor total"
            ))
            for linha in self.__lista:
                escritor.writerow(linha.get_linha())

    def add_locacao(self, nova_locacao: Locacao) -> None:
        nova_locacao.set_id_carro(len(self.__lista))
        self.__lista.append(nova_locacao)
        self.salvar_csv()

    def tam(self) -> int:
        return len(self.__lista)
        
    def seguro(self, id_locacao: int) -> str:
        if id_locacao < 0:
            raise ValueError('Id inválido')
        i = 0
        while i < self.tam() and int(self.__lista[i]['IdLocacao']) != id_locacao:
            i += 1
        if i == self.tam():
            raise ValueError("Esse Id não existe")
        else:
            return str(self.__lista[i]['Seguro'])

    def get_lista(self) -> list:
        return self.__lista
