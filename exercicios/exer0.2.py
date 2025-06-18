'''
Crie um dicionario, voc~e irá inserir palavras e significados para estas palavras,
ao executar o programa, o usuario será perguntado qual palavra ele quer saber o 
significado. Caso a palavra esteja no dicionario, ele apresentara o significado desta
palavra na tela, caso contrario, ele ira exibir uma mensagem, dizendo que não possui 
a palavra em seu dicionario.
'''

dicionario:dict = {
    'Ofuscar': 'Perder ou fazer perder o brilho, a luminosidade ou a visibilidade de algo.',
    'Idílico': 'Que é simples, ingênuo ou puro.',
    'Efemérides': 'Acontecimentos importantes ocorridos no mesmo dia, mas em anos diferentes.'
}

palavra:str = str(input('Qual palavra quer saber o significado: ')).title()
if palavra in dicionario:
    print(f'O significado de {palavra} é: {dicionario[palavra]}')
else:
    print('Não possui a palavra em seu dicionario')
