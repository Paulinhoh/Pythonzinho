'''
Crie um joguinho de par ou impar, o programa irá perguntar ao primeiro jogador se
ele quer par ou impar, depois irá perguntar qual numero ele quer jogar, logo pedira ao
segundo jogador outro numero, fara a soma, utilizando o mesmo modulo do exercicio anterior
e dirá o resultado.
'''

def sum(num1, num2):
    return num1 + num2

joagador1 = str(input("Jogador 1, você quer par ou impar? ")).lower()
joagador1_num = int(input("Jogador 1, qual numero você quer jogar? "))
joagador2_num = int(input("Jogador 2, qual numero você quer jogar? "))

soma = sum(joagador1_num, joagador2_num)
print(f'Resultado -> {soma}')

if soma % 2 == 0 and joagador1 == "par":
    print(f"Jogador 1 venceu")
elif soma % 2 != 0 and joagador1 == "impar":
    print(f"Jogador 1 venceu")
else:
    print(f"Jogador 2 venceu")
