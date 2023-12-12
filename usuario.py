from Professores import Professores
from BancoDeDados import BancoDeDados
from Exceções import LoginUserError, LoginPasswordError, SenhaBrancaError, nomeEmBranco
import pickle
import time

class Usuario:
    def __init__(self, nome_de_usuario, senha, nome):
        self.nome_de_usuario = nome_de_usuario
        self.__senha = senha
        self.nome = nome
        self.adm = False

    @property
    def senha(self):
        return self.__senha
    
    @staticmethod
    def listar_usuarios():
        try:
            with open('usuarios.pickle', 'rb') as file:
                usuarios = pickle.load(file)
        except (FileNotFoundError, EOFError):
            usuarios = []
        return usuarios
    
    @staticmethod
    def cadastrar_usuarios(nome_de_usuario, senha, nome):
        usuarios = Usuario.listar_usuarios()
        novo_usuario = Usuario(nome_de_usuario,senha,nome)
        usuarios.append(novo_usuario)
        Usuario.salvar_usuarios(usuarios)
        print(f"Usuário {nome_de_usuario} cadastrado com sucesso.")

    @staticmethod
    def salvar_usuarios(usuarios):
        with open('usuarios.pickle', 'wb') as file:
            pickle.dump(usuarios, file)

    @staticmethod
    def criar_usuario():
        usuarios = Usuario.listar_usuarios()
        nome = input("Digite seu nome completo: ")
        j = 0
        while j == 0:
            try:
                nome_usuario = input("Digite o seu nome de usuario: ")
                if nome_usuario == "":
                    raise nomeEmBranco
               
                for usuario in usuarios:
                    if usuario.nome_de_usuario == nome_usuario:
                        raise LoginUserError
                   
                j += 1


            except nomeEmBranco:
                print("nome de usuario em branco")
            except LoginUserError:
                print('Nome de usuário não disponível')

        i = 0
        while i == 0:
            senha = input('Insira sua senha: ')
            try:
                confirmar_senha = input('Confirme sua senha: ')
                if confirmar_senha == "":
                    raise SenhaBrancaError                
                if confirmar_senha != senha:
                    raise LoginPasswordError
                i += 1
            except SenhaBrancaError:
                print("senhas invalidas, digite algo")                
            except LoginPasswordError:
                print('Suas senhas não batem')
        
        Usuario.cadastrar_usuarios(nome_usuario, senha, nome)

    @staticmethod
    def entrar_conta(nome_busca):
        try:
            usuarios = Usuario.listar_usuarios()
            logado = 0
            for usuario in usuarios:
                if usuario.nome_de_usuario == nome_busca:
                    try:
                        senha = input('Digite sua senha: ')
                        if usuario.nome_de_usuario == "" or usuario.senha == "":
                            raise SenhaBrancaError
                        if usuario.senha != senha:
                            raise LoginPasswordError
                        logado += 1
                    except SenhaBrancaError:
                        print("usuario ou senha em branco,digite algo")
                    except LoginPasswordError:
                        print('Sua senha está incorreta \nTente novamente em 5 segundos')
                        t = 5
                        while t > 0:
                            print (t)
                            t -= 1
                            time.sleep(1)
                            return

                if logado == 1:
                    print(f"Usuário {nome_busca} está logado.")
                    return True
            else:
                print(f"Nome de usuário {nome_busca} não encontrado. \nTente novamente em 5 segundos")
                t2 = 5
                while t2 > 0:
                    print (t2)
                    t2 -= 1
                    time.sleep(1)


        except FileNotFoundError:
            print("Arquivo de contatos não encontrado.")

class Admnistrador(Usuario):
    def __init__(self,nome_de_usuario,senha,nome):
        super.__init__(nome_de_usuario,senha,nome)
        self.adm = True

    @property
    def adm(self):
        return self.__adm
    
    @staticmethod
    def excluir_comentario(nome_professor):
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome_professor:
                print('Lista de comentários')
                i=1
                for comentario in professor.comentarios:
                    print(f'{i} - {comentario}')
                    i+=1
                escolha = input('Insira o número do comentário que deseja excluir(ou 0 para sair): ')
                if escolha == '0':
                    return
                if escolha == '1':
                    del professor.comentarios[i-2]
        Professores.salvar_professores(professores)

    @staticmethod
    def banir_user(nome_de_usuario):
        usuarios = Usuario.listar_usuarios()
        i=0
        for usuario in usuarios:
            if usuario.nome == nome_de_usuario:
                del usuarios[i]
            i+=1
        Usuario.salvar_usuarios(usuarios)
    
    @staticmethod
    def cadastrar_professores(nome,materia):
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome:
                return
        novo_professor = Professores(nome,materia)
        professores.append(novo_professor)
        Professores.salvar_professores(professores)
        print(f"Professor {nome} cadastrado com sucesso.")

    @staticmethod
    def cadastrar_materias(materia, codigo):
        verificacao = BancoDeDados.verificar_matéria(codigo)
        if verificacao == True:
            with open("materias.txt", "a", encoding='utf-8') as arquivo:
                arquivo.write(f"{materia},{codigo}\n")

        else:
            print('Essa matéria já existe.')
