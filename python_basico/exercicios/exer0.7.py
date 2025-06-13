'''
Usuarios: Crie uma classe chamada Usuario. Crie dois atributos de nomes primeiro_nome
e ultimo_nome e, então, crie vários outros atributos adicionais que geralmente seriam armazenados
em um perfil de usuário. Escreva um método de nome descricao_usuario() que apresente um resumo das 
informações do usuário. Escreva outro método chamado saudacao_usuario() que mostre uma saudação personalizada
ao usuário. 
Crie várias instancias que representem diferentes usuários e chame os dois métodos para cada usuario.
'''


class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome, email, senha):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.email = email
        self.senha = senha

    def descricao_usuario(self):
        print(f'Nome: {self.primeiro_nome.title()}')
        print(f'Sobrenome: {self.ultimo_nome.title()}')
        print(f'Email: {self.email.lower()}')
        print(f'Senha: {self.senha}')
        
    def saudacao_usuario(self):
        print(f'Olá {self.primeiro_nome} {self.ultimo_nome.title()}')
        


def main():
    usuario1 = Usuario('Paulo', 'Reis', 'phdsreis@gmail.com', '123456')
    usuario2 = Usuario('Ana', 'Reis', 'anaclara@gmail.com', '654321')
    
    usuario1.saudacao_usuario()
    usuario1.descricao_usuario()
    print('')
    usuario2.saudacao_usuario()
    usuario2.descricao_usuario()


if __name__ == '__main__':
    main()
