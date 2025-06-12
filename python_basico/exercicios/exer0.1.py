'''
Crie um programa para elaborar uma lista de convidados de uma festa, o programa irá
perguntar o nome do convidado, voc/~e digitará o nome e ao terminar a lista, o programa 
irá exibir a lista em ordem alfabética. Insira até 10 nomes.
'''

convidados:list = []
quantidade_convidados:int = int(input('Quantos convidados você quer adicionar? '))

for i in range(quantidade_convidados):
    nome:str = str(input('Digite o nome do convidado: ')).title()
    convidados.append(nome)

convidados.sort()
print(convidados)
