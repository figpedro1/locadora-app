from classes.Carros import *
from datetime import datetime
import random
import string

modelos = (
    "Kwid",
    "Polo",
    "Renegade",
    "T-Cross",
    "Corolla",
    "Hilux"
)

cores = ("Preto", "Cinza")

cambio = ("Manual", "Automático")

categoria = ("Econômico", "Intermediário", "Conforto", "Pickup")

carros = Carros("../planilhas/Carros.csv")

ano_atual = datetime.now().year

qtd_carros = int(input("Quantos carros deseja gerar? "))

for i in range(carros.tam(), carros.tam() + qtd_carros):
    novo = Carro(vazio=True)
    novo.set_modelo(random.choice(modelos))
    novo.set_cor(random.choice(cores))
    novo.set_ano(ano_atual - random.randint(-1, 3))
    segmentado = []
    for c in range(0, 3):
        segmentado.append(random.choice(string.ascii_uppercase))

    segmentado.append("-")
    numero_placa = 0

    for c in range(0, 4):
        numero_placa = (numero_placa * 10) + random.randint(0, 9)

    numero_placa = str(numero_placa)
    if len(numero_placa) < 4:
        numero_placa = "0" * (4 - len(numero_placa)) + numero_placa
    placa = "".join(segmentado) + numero_placa

    novo.set_placa(placa)
    novo.set_cambio(random.choice(cambio))
    novo.set_categoria(random.choice(categoria))
    novo.set_quilometragem(random.randint(0, 70000))
    novo.set_diaria(round(random.uniform(100, 1000), 2))
    novo.set_seguro(round(random.uniform(100, 1000), 2))
    novo.set_disponivel(True)
    carros.add_carro(novo)

carros.salvar_csv()

