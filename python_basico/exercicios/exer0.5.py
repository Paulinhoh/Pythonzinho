'''
Crie uma classe chamada Restaurante. O med=todo __init__() de Restaurante deve armazenar
dois atributos: restaurante_nome e cozinha_tipo. Crie um método chamado restaurante_descricao()
que mostre essas duas informações, e um método de nome restaurante_aberto() que exibe uma mensagem informando se o restaurante está aberto. Crie uma instancia chamada partir da sua classe. Mostre os dois atributos individualmente e, em seguida, chame os dois métodos.
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
    poke = Restaurante('Poki', 'Japonesa')
    
    print(poke.restaurante_nome)
    print(poke.cozinha_tipo)
    
    poke.restaurante_descricao()
    poke.restaurante_aberto()
    


if __name__ == '__main__':
    main()
