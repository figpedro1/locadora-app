from Clientes import *
from Carros import *
import datetime

class Locacao:
    """
    Classe para iniciar uma nova locação
    Todos os atributos são privados, como denota o prefixo "__".
    Set's são utilizados para atribuir valores aos atributos,
    Get's são utilizados para devolver os valores dos atributos.

    Atributos
    ---------------
        __cpf_cliente: str = cpf do cliente que deseja fazer uma nova locação
    
    """
    
    '''
    Código lixo, caso precise usar depois:
    __idLocacao: int | None = None
    __idCarro: int | None = None
    __cpfCliente: str | None = None
    __dataLocacao: dict = None
    __dataDevolucao: dict | None = {'dia': 0, 'mes': 0, 'ano': 0, 'hora': 0}
    __kmInicial: int | None = None
    __kmFinal: int | None = None
    __seguro: str | None = "Não"
    __valorTotal: float = 0

    #Set e Get do id da Locação
    def set_idLocacao(self, novoIdLocacao: int) -> None:
        novoIdLocacao = int(novoIdLocacao)
        if novoIdLocacao < 0:
            raise ValueError("Id não pode ser negativo")
        self.__idLocacao = novoIdLocacao
    
    def get_idLocacao(self) -> int:
        return self.__idLocacao
    '''
    __cpf_cliente: str | None = None
    __categoria: str | None = None
    __cambio: str | None = None
    __seguro: str | None = None
    __disponivel: bool = False

    def __init__(self, 
                 cpf_cliente: str | None =None,
                 categoria: str | None = None,
                 cambio: str | None = None,
                 seguro: str | None = None,
                 vazio: bool = False
                 ) -> None:
        if not vazio:
            self.set_cpf_cliente(cpf_cliente)
            self.set_categoria(categoria)
            self.set_cambio(cambio)
            self.set_seguro(seguro)

    #Set e Get do CPF do cliente
    def set_cpf_cliente(self, novoCpf: str) -> None:
        """
        Atribui o CPF do cliente na classe Locações
        """
        self.__cpf_cliente = Cliente.formatar_cpf(novoCpf)

    def get_cpf_cliente(self) -> str:
        return self.__cpf_cliente

    def set_categoria(self, ctgoria: str) -> None:
        if str(ctgoria).upper() not in ("ECONÔMICO", "ECONOMICO", "INTERMEDIÁRIO", "INTERMEDIARIO", "CONFORTO", "PICKUP"):
            raise ValueError("Categoria inválida")
        if str(ctgoria).upper() == "ECONOMICO":
            ctgoria = "Econômico"
        if str(ctgoria).upper() == "INTERMEDIARIO":
            ctgoria = "Itermediário"
        self.__categoria = str(ctgoria).capitalize()
    
    def get_categoria(self) -> str:
        return self.__categoria

    def set_cambio(self, cambio: str) -> None:
        if str(cambio).upper() not in ("MANUAL", "AUTOMÁTICO", "AUTOMATICO"):
            raise ValueError("Câmbio inválido")
        if str(cambio).upper() == "AUTOMATICO":
            cambio = "Automático"
        self.__cambio = cambio.capitalize()
    
    def get_cambio(self) -> str:
        return self.__cambio

    def set_seguro(self, seguro: str) -> None:
        if str(seguro).upper() not in ("SIM", "NÃO", "NAO"):
            raise ValueError("Resposta inválida")
        if str(seguro).upper() == "NAO":
            seguro = "Não"
        self.__seguro = str(seguro).capitalize()
    
    def get_seguro(self) -> str:
        return self.__seguro
    

#Testando a classe de locacao
nova_locacao = Locacao(cpf_cliente=str(input('Digite seu cpf: ')), 
                       categoria=str(input('Digite a categoria: ')),
                       cambio=str(input('Digite o câmbio: ')),
                       seguro=str(input('Deseja seguro?\nSIM | NÃO\n')))

print('-'*30)
print(nova_locacao.get_cpf_cliente())

#Testando como pegar a lista de carros, necessário para a pesquisa de carros disponíveis com o câmbio e categoria desejada do cliente
lista_carro = Carros(caminho_para_arquivo=".\locadora_app\Carro.csv")
print(lista_carro.get_carro(1))