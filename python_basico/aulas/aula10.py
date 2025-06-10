# ---------------------------------------------------------------------------------------------
# Fatiando listas

alimentos:list = ['banana', 'maçã', 'laranja', 'uva', 'morango', 'abacaxi', 'melancia']

print(alimentos[2:4]) # [2, 4)
print(alimentos[2:]) # [2, 6]
print(alimentos[:4]) # [0, 4)
print(alimentos[::2]) # pegando todos os elementos pulando de 2 em 2
print(alimentos[-3:]) # [4, 6]

for alimento in alimentos[:5]:
    print(alimento)
