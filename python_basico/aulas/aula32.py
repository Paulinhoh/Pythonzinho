# ---------------------------------------------------------------------------------------------
# Herança - Parte 2


# classe pai
class Carros():
    """Uma tentativa simples de representar um carro."""
    
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 100
        self.odometro = 0
    
    
    def decricao_nome(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        nome_longo = f"{self.ano} {self.fabricante} {self.modelo}"
        return nome_longo.title()
    
    
    def leia_odometro(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        return f"Este carro tem {self.odometro} quilometros rodados."
    
    
    def altera_odometro(self, novo_odometro):
        """Altera o odometro pelo valor passado pelo argumento."""
        self.odometro = novo_odometro
    
    
    def incrementa_odometro(self,novo_odometro):
        """Incrementa um determinado valor ao odometro."""
        self.odometro += novo_odometro
    
    
    def tanque_gasolina(self):
        """Exibe a quantidade de gasolina no tanque."""
        print(f"O tanque de gasolina esta {self.combustivel}% cheio.")


# classe filho
class CarrosEletrico(Carros):
    """Representa aspectos de um carro especificos de carros eletricos."""
    
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos da classe pai."""
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

    def tanque_gasolina(self):
        """Carros eletricos não tem tanque de gasolina."""
        print("Este carro não precisa de tanque de gasolina.")


class Bateria():
    """Uma tentativa simples de modelar uma bateria."""
    
    def __init__(self, bateria=100):
        """Inicializa os atributos da bateria."""
        self.bateria = bateria

    
    def altera_bateria(self, nova_bateria):
        """Altera o valor da bateria."""
        self.bateria = nova_bateria
    
    
    def mostrar_bateria(self):
        print(f"A bateria esta {self.bateria}% cheia.")
