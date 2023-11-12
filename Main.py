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
        criar_user = bancodedados.criar_user()
        novo_user = Usuario(criar_user[0],criar_user[1],criar_user[2])
        bancodedados.adc_usuarios(novo_user)
        bancodedados.listar_usuarios()
                
    if comando == '2':
        dados = bancodedados.entrar()
        print(dados)
        user_ativo = Usuario(dados[0],dados[1])
        user_ativo.logar()

    if comando == '3':
        break
