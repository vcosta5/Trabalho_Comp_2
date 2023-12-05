from Professores import Professores
from BancoDeDados import BancoDeDados
from usuario import Usuario, Admnistrador

BancoDeDados.criar_materias()
BancoDeDados.criar_professores_instancia()


def navegacao(nome_de_usuario):
    while True:
        print(f'1 -> Ver lista de matérias \n2 -> Ver lista completa de professores \n3 -> Operações por matéria \n4 -> Sair')
        opcao = input('Insira o comando: ')
        if opcao == '1':
            BancoDeDados.visualizar_materias()
        if opcao =='2':
            professores = Professores.listar_professores()
            if not professores:
                print("Nenhum professor cadastrado.")
            else:
                print("Lista de Professores:")
                for professor in professores:
                    print(f"Nome: {professor.nome}, Matéria: {professor.materia}, Avaliação: {professor.avaliação}")
        if opcao == '3':
            k = 0
            while k == 0:
                codigo = input('Insira o código da matéria (Ou digite 0 para sair): ')

                if codigo == '0':
                    k += 1
                
                else:
                    nome_materia = BancoDeDados.verificar_matéria(codigo)
                    print(f"===== Professores de {nome_materia} =====\n")
                    professores_materia = Professores.consultar_professor_materia(nome_materia)
                    for professor in professores_materia:
                        print(f"Nome: {professor.nome}, Matéria: {professor.materia}, Avaliação: {professor.avaliação}")
                    
                    j = 0
                    while j == 0:
                        print(f'1 -> Ver detalhes do professor \n2 -> Avaliar Professor \n3 -> Listar professores de {nome_materia} \n4 -> Voltar')
                        comando = input('Insira o comando: ')

                        if comando == '1':
                            nome = input(f'Insira o nome do professor de {nome_materia} que você quer visualizar: ')
                            i=0
                            for professor in professores_materia:
                                if professor.nome == nome:
                                    professor = Professores.consultar_professor_nome(nome)
                                    if professor:
                                        print(f"Nome: {professor.nome}, Matéria: {professor.materia}, Avaliação: {professor.avaliação}")
                                        print('Comentários: ')
                                        for comentario in professor.comentarios:
                                            print(comentario)
                                        i+=1
                            if i == 0:
                                print(f'Esse professor não dá aula de {nome_materia}')
                        
                        if comando == '2':
                            i=0
                            nome = input("Digite o nome do professor que deseja avaliar: ")
                            for professor in professores_materia:
                                if professor.nome == nome:
                                    Professores.avaliar_professor(nome, nome_de_usuario)
                                    i+=1
                            if i == 0:
                                print(f'Esse professor não dá aula de {nome_materia}')

                        if comando == '3':
                            print(f"===== Professores de {nome_materia} =====\n")
                            professores_materia = Professores.consultar_professor_materia(nome_materia)
                            for professor in professores_materia:
                                print(f"Nome: {professor.nome}, Matéria: {professor.materia}, Avaliação: {professor.avaliação}")                    

                        if comando == '4':
                            j += 1
        if opcao == '4':
            print(f'{nome_de_usuario} saiu.')
            return


while True:
    print('1 -> Criar conta \n2 -> Entrar na conta \n3 -> Sair')
    comando = input('Insira seu comando: ')

    if comando == '1':
        criar_user = Usuario.criar_usuario()
                
    if comando == '2':
        nome = input('Insira seu nome de usuário: ')
        login = Usuario.entrar_conta(nome)
        if login == True:
            navegacao(nome)

    if comando == '3':
        break
