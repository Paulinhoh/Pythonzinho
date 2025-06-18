# ---------------------------------------------------------------------------------------------
# Instrução break e continue

while True:
    print('Para encerrar digite "sair')
    cidade:str = str(input('Digite uma cidade: ')).lower()
    
    if cidade == 'continuar':
        continue
    elif cidade == 'sair':
        break
    else:
        print(f'A cidade digitada foi: {cidade}')

print('Fim do programa')
