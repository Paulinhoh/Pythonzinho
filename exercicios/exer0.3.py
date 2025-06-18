'''
Crie uma calculadora com 4 operações, div, sub, som, mult, que pergunte ao usuario
qual operação ele deseja realizar e peça os numeros que serão calculados, em seguida
mostre o resultado da operação na tela, sendo que as funções utilizadas no prorama
estejam em um modulo separado do arquivo principal.
'''

from ..aulas import aula23

ope:str = str(input('Qual operação deseja realizar [som/sub/mult/div]: ')).lower()
num1:float = float(input('Digite o primeiro numero: '))
num2:float = float(input('Digite o segundo numero: '))

if ope == 'som':
    aula23.soma(num1, num2)
elif ope == 'sub':
    aula23.subtracao(num1, num2)
elif ope == 'mult':
    aula23.multiplicacao(num1, num2)
elif ope == 'div':
    aula23.divisao(num1, num2)

