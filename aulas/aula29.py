# ---------------------------------------------------------------------------------------------
# Alterando atributos de uma instância - Parte 1

class Carros():
    """Uma tentativa simples de representar um carro."""
    
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0
        
    def decricao_nome(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        nome_longo = f"{self.ano} {self.fabricante} {self.modelo}"
        return nome_longo.title()
    
    def leia_odometro(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        return f"Este carro tem {self.odometro} quilometros rodados."


meu_carro = Carros('audi', 'a4', 2019)
print(meu_carro.decricao_nome())
print(meu_carro.leia_odometro())

print("")
print("Mudando o odometro")
meu_carro.odometro = 5
print(meu_carro.leia_odometro())
