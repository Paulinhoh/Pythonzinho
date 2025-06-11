# ---------------------------------------------------------------------------------------------
# If e Else part 1

cor:str = 'azul'
num:int = 0

if num == 1:
    if cor == 'azul':
        print('A cor é azul')
    elif cor == 'verde':
        print('A cor é verde')
    elif cor == 'amarelo':
        print('A cor é amarelo')
    else:
        print('A cor não é azul')
else:
    print('O número não é 1, portanto não é possível verificar a cor')

print('A cor é azul' if cor == 'azul' else 'A cor não é azul') # ternario
