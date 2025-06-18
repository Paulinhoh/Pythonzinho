# ---------------------------------------------------------------------------------------------
# Argumentos posicionais, nomeados e padrões

def animais(especie='gato', nome=''):
    print(f'Eu tenho um {especie} e ele se chama {nome}')

animais('cachorro', 'Toby')
animais('gato', 'Aquiles')

animais(nome='Nick', especie='cachorro')
animais(nome = 'Garfield')


def nome_completo(nome='', nome_do_meio='', sobrenome=''):
    if nome_do_meio == '':
        print(f'{nome.title()} {sobrenome.title()}')
    else:
        print(f'{nome.title()} {nome_do_meio.title()} {sobrenome.title()}')
    
nome_completo('joão', 'da', 'silva')
nome_completo('Paulo', sobrenome='Reis')
