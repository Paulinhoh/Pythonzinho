# ---------------------------------------------------------------------------------------------
# Manipulando Arquivos de texto

arquivo = open("aula34.txt", "r")

for linha in arquivo:
    print(linha)

arquivo.close()

# outra forma de abrir o arquivo que fecha automaticamente
with open("aula34.txt", "a") as arquivo:
    texto = str(input("Digite um texto: "))
    arquivo.write(f"{texto}\n")

