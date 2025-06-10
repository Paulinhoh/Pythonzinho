# ---------------------------------------------------------------------------------------------
# Trabalhando com números no laço FOR

numeros:list = list(range(0, 21, 2))
print(numeros)

for numero in numeros:
    print(numero)
    
print('Fim do programa')

print('\nOutra maneirra de fazer\n')

for numero in range(0, 21, 2):
    print(numero)
    
print('Fim do programa')

print('=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

numeros_par:list = list(range(0, 21, 2))
print(numeros_par)

print('Outra maneirra de fazer')

numeros_par2 = []
for numero in range(0, 21, 2):
    numeros_par2.append(numero)
    
print(numeros_par2)
