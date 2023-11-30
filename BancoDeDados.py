from Exceções import TimMaiaError, LoginEmptyError, LoginPasswordError, LoginUserError
from Professores import Professores

class BancoDeDados:

    def visualizar_usuarios():
        try:
            with open("usuarios.txt", "r") as arquivo:
                usuarios = arquivo.readlines()
                if usuarios:
                    print("Lista de usuários:")
                    for usuario in usuarios:
                        nome_de_usuario, senha, nome = usuario.strip().split(",")
                        print(f"Nome de usuário: {nome_de_usuario}, Senha: {senha}, Nome: {nome}")
                else:
                    print("Nenhum usuario encontrado.")
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado.")

    def criar_usuario():
        nome = input("Digite seu nome completo: ")
        j = 0
        while j == 0:
            try:
                nome_usuario = input("Digite o seu nome de usuario: ")
                verificacao = BancoDeDados.verificar_usuario(nome_usuario)
                if verificacao == False:
                    raise TimMaiaError
                j += 1
            except TimMaiaError:
                print('Nome de usuário não disponível')

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
        
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{nome_usuario},{senha},{nome}\n")
        
        print("Usuário criado com sucesso!")

    def verificar_usuario(nome_busca):
        try:
            with open("usuarios.txt", "r") as arquivo:
                usuarios = arquivo.readlines()
                for usuario in usuarios:
                    nome, _, _ = usuario.strip().split(",")
                    if nome == nome_busca:
                        return False
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado.")
            return True

    def entrar_conta(nome_busca):
        try:
            with open("usuarios.txt", "r") as arquivo:
                usuarios = arquivo.readlines()
            with open("contatos.txt", "w") as arquivo:
                logado = 0
                for usuario in usuarios:
                    nome_de_usuario, senha, nome = usuario.strip().split(",")
                    if nome_de_usuario == nome_busca:
                        teste_senha = input(f"Digite a sua senha: ")

                        #i = 0
                        #while i == 0:
                        try:
                            if teste_senha != senha:
                                raise LoginPasswordError
                            logado += 1
                            #i += 1
                        except LoginPasswordError:
                            print('Sua senha está incorreta')
                if logado == 1:
                    print(f"Usuário {nome_busca} está logado.")
                    return True
                else:
                    print(f"Nome de usuário {nome_busca} não encontrado.")
        except FileNotFoundError:
            print("Arquivo de contatos não encontrado.")

    def criar_materias():
        with open("materias.txt", "w", encoding='utf-8') as arquivo:
            arquivo.write(f"Física 1,FIT112\n")
            arquivo.write(f"Física 2,FIT122\n")
            arquivo.write(f"Física 3,FIM230\n")
            arquivo.write(f"Física 4,EEU240\n")
            arquivo.write(f"Cálculo 1,MAC118\n")
            arquivo.write(f"Cálculo 2,MAC128\n")
            arquivo.write(f"Cálculo 3,MAC238\n")
            arquivo.write(f"Cálculo 4,MAC248\n")
            arquivo.write(f"Álgebra linear,MAE125\n")
            arquivo.write(f"Química,IQG111\n")

    def visualizar_materias():
        try:
            with open("materias.txt", "r", encoding = 'utf-8') as arquivo:
                materias = arquivo.readlines()
                if materias:
                    print("Lista de matérias:")
                    print('\n')
                    i = 1
                    for materia in materias:
                        nome_materia, codigo = materia.strip().split(",")
                        print(f"{i}--> {nome_materia}, Código: {codigo}")
                        i += 1
                else:
                    print("Nenhuma matéria encontrada.")
        except FileNotFoundError:
            print("Arquivo de matérias não encontrado.")

    def verificar_matéria(codigo_busca):
        try:
            with open("materias.txt", "r", encoding='utf-8') as arquivo:
                materias = arquivo.readlines()
                for materia in materias:
                    nome, codigo = materia.strip().split(",")
                    if codigo == codigo_busca:
                        return nome
        except FileNotFoundError:
            print("Matéria não encontrada.")
            return True

    def criar_professores_instancia():
        Professores.cadastrar_professor('Wellington','Física 1')
        Professores.cadastrar_professor('Juninho','Física 1')
        Professores.cadastrar_professor('Robson','Física 2')
        Professores.cadastrar_professor('Drogba','Física 2')
        Professores.cadastrar_professor('Adriano','Física 3')
        Professores.cadastrar_professor('Milena','Física 3')
        Professores.cadastrar_professor('Rodolfo','Física 4')
        Professores.cadastrar_professor('Jorge','Física 4')
        Professores.cadastrar_professor('Ana','Cálculo 1')
        Professores.cadastrar_professor('Claudia','Cálculo 1')
        Professores.cadastrar_professor('Rafaela','Cálculo 2')
        Professores.cadastrar_professor('Neymar','Cálculo 2')
        Professores.cadastrar_professor('Gabigol','Cálculo 3')
        Professores.cadastrar_professor('Sara','Cálculo 3')
        Professores.cadastrar_professor('Alan','Cálculo 4')
        Professores.cadastrar_professor('Ricardo','Cálculo 4')
        Professores.cadastrar_professor('Bruna','Álgebra linear')
        Professores.cadastrar_professor('Isabela','Álgebra linear')
        Professores.cadastrar_professor('Leonardo','Química')
        Professores.cadastrar_professor('Careca','Química')

    def verificar_professores(materia_busca):
        lista_professores = []
        try:
            with open("professores.txt", "r", encoding= 'utf-8') as arquivo:
                professores = arquivo.readlines()
                for professor in professores:
                    lista_busca = professor.strip().split(",")
                    if materia_busca in lista_busca:
                        lista_professores.append(lista_busca[0])
                print(lista_professores)
                return lista_professores
        except FileNotFoundError:
            print("Professores não encontrados.")
            return True
