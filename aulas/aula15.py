# ---------------------------------------------------------------------------------------------
# If e Else part 3

idade:int = int(input("Digite sua idade: ")) # entrada de dados pelo usuario

if idade >= 16 and idade < 18 or idade > 70:
    print("Voto opcional!")
elif idade >= 18 and idade <= 70:
    print("Voto obrigatório!")
else:
    print("Você não pode votar!")
