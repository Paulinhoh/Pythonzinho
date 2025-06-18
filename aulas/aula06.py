# ---------------------------------------------------------------------------------------------
# Manipulando elementos de uma lista

carros:list = ['Ferrari', 'Porsche', 'BMW']
print(carros)

carros[1] = 'Lamborghini' # substitui o valor da posição 1
print(carros)

carros.append('Porsche') # adiciona um valor ao final da lista
print(carros)

carros.insert(1, 'Audi') # adiciona um valor na posição especificada
print(carros)

carros.extend(['Fusca']) # adiciona um valor ao final da lista
print(carros)

carros.remove('Fusca') # remove um valor da lista
print(carros)

del carros[2] # remove um valor da lista
print(carros)

carros.pop() # remove o último valor da lista
print(carros)

carros.pop(1) # remove o valor da   
print(carros)
