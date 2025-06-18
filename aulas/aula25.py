# ---------------------------------------------------------------------------------------------
# Valor de retorno das funções (return)

def nome_completo(nome='', nome_do_meio='', sobrenome=''):
    if nome_do_meio == '':
        return f'{nome.title()} {sobrenome.title()}'
    else:
        return f'{nome.title()} {nome_do_meio.title()} {sobrenome.title()}'
    
nome = nome_completo('Paulo', 'Henrique', 'Reis')
print(nome)


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

soma = soma(5, 3)
sub = subtracao(10, 7)
mult = multiplicacao(2, 5)
div = divisao(20, 4)

conta_final = mult + sub
print(conta_final)
