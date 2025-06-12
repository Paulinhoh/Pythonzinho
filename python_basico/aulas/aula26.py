# ---------------------------------------------------------------------------------------------
# Trabalhando com listas dentro de funções

def lista_funcao(lista):
    for valor in lista:
        print(valor)
        lista.pop()
    print(lista)

cores:list = ['Vermelho', 'Verde', 'Preto', 'Branco', 'Azul']
lista_funcao(cores.copy())
print(cores)
