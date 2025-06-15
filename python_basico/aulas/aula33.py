# ---------------------------------------------------------------------------------------------
# Herança - Parte 3

# import aula32
# from aula32 import *
from aula32 import CarrosEletrico

meu_carro = CarrosEletrico('Tesla', 'model s', 2022)
meu_carro.bateria.mostrar_bateria()
meu_carro.bateria.altera_bateria(80)
meu_carro.bateria.mostrar_bateria()
