# ---------------------------------------------------------------------------------------------
# If e Else part 4

ingredientes:list = ['mostarda', 'tomate', 'queijo']
ingredientes_pedido:list = ['queijo', 'tomate', 'mostarda', 'pimentão']

for ingrediente in ingredientes_pedido:
    if ingrediente in ingredientes:
        print(f'Adicionando {ingrediente} a sua pizza')
    else:
        print(f'Desculpe, não temos {ingrediente} em estoque')
    
print('Sua pizza está pronta')
