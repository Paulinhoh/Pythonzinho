# ---------------------------------------------------------------------------------------------
# Copiando listas

alimentos:list = ['Tomate', 'Batata', 'Uva', 'Banana', 'Ovos', 'Pão', 'Pizza']

alimentos2 = alimentos.copy() # copia a lista
alimentos3 = alimentos[:] # copia a lista
alimentos4 = alimentos


print(alimentos)
print(alimentos2)
print(alimentos3)
print(alimentos4)

alimentos.append('Cenoura')

print(alimentos)
print(alimentos2)
print(alimentos3)
print(alimentos4)

