# ---------------------------------------------------------------------------------------------
# Dicionarios part 2

alien_0:dict = {'cor': 'azul', 'pontos': 5, 'x_pos': 0, 'y_pos': 25, 'poder':'fogo'}
print(alien_0)

print('=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
del alien_0['poder'] # deleta o item do dicionario
print(alien_0)

print('=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for key, value in alien_0.items():
    print(f'Chave: {key}')
    print(f'Valor: {value}')

print('=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for key in alien_0.keys():
    print(key)

print('=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for value in alien_0.values():
    print(value)


