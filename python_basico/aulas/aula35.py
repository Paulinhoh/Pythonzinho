# ---------------------------------------------------------------------------------------------
# Tratamento de erros com Try e Except

import aula23

continuar = ''
while True:
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
    else:
        try:
            operacao = int(input('Digite a operação desejada: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \n--> '))
            if operacao == 1:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'{num1} + {num2} = {aula23.soma(num1, num2)}')
                print('')
            elif operacao == 2:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'{num1} - {num2} = {aula23.subtracao(num1, num2)}')
                print('')
            elif operacao == 3:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'{num1} * {num2} = {aula23.multiplicacao(num1, num2)}')
                print('')
            elif operacao == 4:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                print(f'{num1} / {num2} = {aula23.divisao(num1, num2)}')
                print('')
            else:
                print('Opção invalida!')
        
        except ValueError:
            print('Ocorreu algum erro inesperado!')

print('Fim do programa')
