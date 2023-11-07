from usuario import Usuario, Administrador, User
from Professor import Professor
from Materia import Materia
from Exceções import TimMaiaError
from BancoDeDados import BancoDeDados

adm1 = Administrador('Vinícius Costa', 'abc123', 'Vcosta1')

usuarios = [adm1]
materias = []
professores = []
bancodedados = BancoDeDados(usuarios, materias, professores)

while True:
    print('1 -> Criar conta \n2 -> Entrar na conta \n3 -> Sair')
    comando = input('Insira seu comando: ')

    if comando == '1':
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

        novo_user = Usuario(nome, senha, nome_de_usuario)
        bancodedados.adc_usuarios(novo_user)
        bancodedados.listar_usuarios()
                
    if comando == '2':
        pass

    if comando == '3':
        break
