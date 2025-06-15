# ---------------------------------------------------------------------------------------------
# Herança - Parte 1

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


carro1 = Carros("honda", "civic", 2020)
carro1.tanque_gasolina()

class CarroEletrico(Carros):
    """Representa aspectos de um carro especificos de carros eletricos."""
    
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos da classe pai."""
        super().__init__(fabricante, modelo, ano)
    
    
    def tanque_gasolina(self):
        """Carros eletricos não tem tanque de gasolina."""
        print("Este carro não precisa de tanque de gasolina.")


print("")
carro_eletrico = CarroEletrico("tesla", "model s", 2019)
print(carro_eletrico.decricao_nome())
carro_eletrico.tanque_gasolina()
