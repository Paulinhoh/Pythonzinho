# ---------------------------------------------------------------------------------------------
# If e Else part 5

ingredientes_pedido:list = []
continuar:str = 's'

while True:
    ingrediente:str = str(input('Digite um ingrediente: ')).lower()
    ingredientes_pedido.append(ingrediente)
    
    continuar = str(input('Deseja continuar? [s/n] ')).lower()
    if continuar == 'n':
        break


ingredientes:list = ['mostarda', 'tomate', 'queijo']
for ingrediente in ingredientes_pedido:
    if ingrediente in ingredientes:
        print(f'Adicionando {ingrediente} a sua pizza')
    else:
        print(f'Desculpe, não temos {ingrediente} em estoque')
    
print('Sua pizza está pronta')

