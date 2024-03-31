class Locacoes:
    '''__id_locacao = None
    __carro = None
    __locatario = None
    __data_locacao = None
    __data_devolucao = None
    __km_inicial = None
    __km_final = None
    __seguro = None
    __valor_total = None
    def __init__(self, id_locacao, id_carro, )
'''

    __idLocacao: int | None = None
    __idCarro: int | None = None
    __cpfCliente: str | None = None
    __dataLocacao: dict = None
    __dataDevolucao: dict | None = {'dia': 0, 'mes': 0, 'ano': 0, 'hora': 0}
    __kmInicial: int | None = None
    __kmFinal: int | None = None
    __seguro: str | None = "Não"
    __valorTotal: float = 0

    def set_idLocacao(self, novoIdLocacao: int) -> int:
        novoIdLocacao = int(novoIdLocacao)
        if novoIdLocacao < 0:
            raise ValueError("Id não pode ser negativo")
        self.__idLocacao = novoIdLocacao
    def get_idLocacao(self) -> int:
        return self.__idLocacao




#Testando a classe de locacao
locacao = Locacoes
novoId = int(input('Digite o id de locacao: '))
locacao.set_idLocacao(locacao, novoId)
print("O id de locacao é: ", locacao.get_idLocacao(locacao))