'''
Três restaurantes: comece com a classe do exercicio anterior. Crie três instancias diferentes 
da classe e chame restaurante_descricao() para cada instancia.
'''


class Restaurante():
    def __init__(self, restaurante_nome, cozinha_tipo):
        self.restaurante_nome = restaurante_nome
        self.cozinha_tipo = cozinha_tipo

    def restaurante_descricao(self):
        print(f'Nome do restaurante: {self.restaurante_nome}')
        print(f'Tipo de cozinha: {self.cozinha_tipo}')
        
    def restaurante_aberto(self):
        print(f'O restaurante {self.restaurante_nome} está aberto.')


def main():
    restaurante1 = Restaurante('Poki', 'Japonesa')
    restaurante2 = Restaurante('Panela De Bairro', 'Cazeira')
    restaurante3 = Restaurante('Dominos', 'Pizzaria')

    restaurante1.restaurante_descricao()
    print('')
    restaurante2.restaurante_descricao()
    print('')
    restaurante3.restaurante_descricao()


if __name__ == '__main__':
    main()
