from Exceções import TimMaiaError, LoginEmptyError, LoginPasswordError, LoginUserError
from usuario import Usuario

class BancoDeDados:
    def __init__(self, lista_usuarios = [], lista_materias = [], lista_professores = []):
        self.lista_usuarios = lista_usuarios
        self.lista_materias = lista_materias
        self.lista_professores = lista_professores

    def adc_usuarios(self, usuario):
        self.lista_usuarios.append(usuario)

    def listar_usuarios(self):
        print('         Lista de usuários         ')
        print('--------------------------------')
        for i in self.lista_usuarios:
            print(f"Nome de usuário: {i.nome_de_usuario}")
        print('--------------------------------')

    
    def listar_materias(self):
        pass

    def listar_professores(self):
        pass

    def criar_user(self):
        nome = input('Insira seu nome completo: ')
        nome_de_usuario = input('Insira seu nome de usuário: ')
        i = 0
        while i == 0:
            senha = input('Insira sua senha: ')
            try:
                confirmar_senha = input('Confirme sua senha: ')
                if confirmar_senha != senha:
                    raise TimMaiaError
                i += 1
            except TimMaiaError:
                print('Suas senhas não batem')
        return [nome_de_usuario, senha, nome]
    
    def entrar(self):
        lista_nomes = []
        j=0 
        while j == 0:
            nome_de_usuario = input('Insira o nome de usuário (Digite 0 para sair): ')
            if nome_de_usuario == '0':
                return
            try:
                if nome_de_usuario == '':
                    raise LoginEmptyError
                
                for i in self.lista_usuarios:
                    lista_nomes.append(i.nome_de_usuario)

                if nome_de_usuario not in lista_nomes:
                    raise LoginUserError
                else:
                    senha = input('Insira a senha: ')
                    for i in self.lista_usuarios:
                        if nome_de_usuario == i.nome_de_usuario:
                            if senha == i.senha:
                                print(f'\nVocê está logado como {i.nome_de_usuario}')
                                return [nome_de_usuario, senha]

                            else:
                                raise LoginPasswordError

            except LoginEmptyError:
                print('Insira algum nome de usuário')

            except LoginUserError:
                print('Esse usuário não existe')

            except LoginPasswordError:
                print('Senha incorreta')    
