# ---------------------------------------------------------------------------------------------
# Classes

class Cachorro():
    """ Uma tentativa simples de modelar um cachorro. """
    
    def __init__(self, nome, idade):
        """ Inicializa os atributos nome e idade. """
        self.nome = nome
        self.idade = idade
    
    
    def sentar(self):
        """ Simula um cachorro sentando. """
        print(f'{self.nome.title()} está sentado.')
        
    
    def rolar(self):
        """ Simula um cachorro rolando em resposta a um comando. """
        print(f'{self.nome.title()} está rolando.')
    


meu_cachorro = Cachorro('Aquiles', 6)

meu_cachorro.sentar()
meu_cachorro.rolar()

meu_outro_cachorro = Cachorro('Luna', 4)

meu_outro_cachorro.sentar()
meu_outro_cachorro.rolar()

