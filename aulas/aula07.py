# ---------------------------------------------------------------------------------------------
# Organizando listas

carros:list = ['Ferrari', 'BMW', 'Mercedes', 'Audi', 'MacLaren']
print(carros)

print(sorted(carros)) # organiza a lista em ordem alfabética
print(carros)

carros.sort() # organiza a lista em ordem alfabética
print(carros)

carros.sort(reverse=True) # organiza a lista em ordem alfabética inversa
print(carros)

carros.reverse() # inverte a ordem da lista
print(carros)

tam:int = len(carros) # retorna o tamanho da lista
print(f'tamamanho da lista: {tam}')
