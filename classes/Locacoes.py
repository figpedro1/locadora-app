from Clientes import Cliente

class Locacoes:
    """
    Classe para todas as locações
    Todos os atributos são privados, como denota o prefixo "__".
    Set's são utilizados para atribuir valores aos atributos,
    Get's são utilizados para devolver os valores dos atributos.

    Atributos
    ---------------
        __idLocacao: int = id da locação, não podendo ser menor do que 0
    
    """
    __idLocacao: int | None = None
    __idCarro: int | None = None
    __cpfCliente: str | None = None
    __dataLocacao: dict = None
    __dataDevolucao: dict | None = {'dia': 0, 'mes': 0, 'ano': 0, 'hora': 0}
    __kmInicial: int | None = None
    __kmFinal: int | None = None
    __seguro: str | None = "Não"
    __valorTotal: float = 0

    def set_idLocacao(self, novoIdLocacao: int) -> None:
        novoIdLocacao = int(novoIdLocacao)
        if novoIdLocacao < 0:
            raise ValueError("Id não pode ser negativo")
        self.__idLocacao = novoIdLocacao
    
    def get_idLocacao(self) -> int:
        return self.__idLocacao

    def set_cpfCliente(self, novoCpf: str) -> None:
        self.__cpfCliente = Cliente.formatar_cpf(novoCpf)

    def get_cpfCliente(self) -> str:
        return self.__cpfCliente
    
    def set_kmInicial(self, kilometragemI: int) -> None:
        kilometragemI = int(kilometragemI)
        if kilometragemI < 0:
            raise ValueError
        self.__kmInicial = kilometragemI

    def get_kmInicial(self) -> int:
        return self.__kmInicial


#Testando a classe de locacao
locacao = Locacoes
novoId = int(input('Digite o id de locacao: '))
kmI = int(input('Digite a kilometragem inicial: '))
cpfCliente = input('Digite seu cpf: ')
locacao.set_idLocacao(locacao, novoId)
locacao.set_cpfCliente(locacao, cpfCliente)
locacao.set_kmInicial(locacao, kmI)
print('-'*40)
print("O id de locacao é: ", locacao.get_idLocacao(locacao))
print('O cpf do cliente é: ', locacao.get_cpfCliente(locacao))
print("O km inicial é: ", locacao.get_kmInicial(locacao))