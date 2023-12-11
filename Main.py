from Professores import Professores
from BancoDeDados import BancoDeDados
from usuario import Usuario, Admnistrador
from Materia import Materia
from Periodo import Periodo

BancoDeDados.criar_materias()
BancoDeDados.criar_professores_instancia()
BancoDeDados.criar_periodos()
BancoDeDados.listas_periodos()

def navegacao(nome_de_usuario):
    while True:
        print(f'1 -> Matérias \n2 -> Professores \n3 -> Sair')
        opcao = input('Insira o comando: ')
        if opcao == '1':
            j = 0 
            while j == 0:
                materias = Materia.listar_materias()
                if not materias:
                    print("Nenhuma matéria cadastrada.")
                else:
                    print('Lista de matérias: ')
                    for materia in materias:
                        print(f'Nome: {materia.nome}  Código: {materia.codigo}') 
                    print(f'1 -> Avaliar matéria \n2 -> Comentar matéria \n3 -> Visualizar matéria por período \n4 -> Voltar')  
                    escolha = input('Insira o comando: ')

                    if escolha == '1':
                        periodos = Periodo.listar_periodos()
                        periodo_input = input('Insira o período (de 21.1 a 23.2): ')
                        j=0
                        for periodo in periodos:
                            if periodo.nome == periodo_input:
                                codigo_input = input('Insira o código da matéria: ')
                                i=0
                                for materia in periodo.materias:
                                    if materia.codigo == codigo_input:
                                        materia.avaliar_materia(codigo_input)
                                        i+=1
                                if i == 0:
                                    print('Matéria não encontrada')
                            j+=1
                        periodo.salvar_periodos(periodos)
                        if j == 0:
                            print('Periodo não encontrado')

                    if escolha == '2':
                        periodos = Periodo.listar_periodos()
                        periodo_input = input('Insira o período (de 21.1 a 23.2): ')
                        j=0
                        for periodo in periodos:
                            if periodo.nome == periodo_input:
                                codigo_input = input('Insira o código da matéria: ')
                                i=0
                                for materia in periodo.materias:
                                    if materia.codigo == codigo_input:
                                        materia.comentar_materia(codigo_input,nome_de_usuario)
                                        i+=1
                            
                                if i == 0:
                                    print('Matéria não encontrada')
                        
                            j+=1
                        periodo.salvar_periodos(periodos)
                        if j == 0:
                            print('Periodo não encontrado')

                    if escolha =='3':
                        periodo_input = input('Insira o período (de 21.1 a 23.2): ')
                        Periodo.visualizar_materias(periodo_input)

                    if escolha =='4':
                        j += 1                

        if opcao =='2':
            j = 0 
            while j == 0:
                professores = Professores.listar_professores()
                if not professores:
                    print("Nenhum professor cadastrado.")
                else:
                    print('Lista de professores: ')
                    for professor in professores:
                        print(f'Nome: {professor.nome}  Matéria: {professor.materia}') 
                    print(f'1 -> Avaliar professor \n2 -> Comentar professor \n3 -> Visualizar professor por período \n4 -> Voltar')  
                    escolha = input('Insira o comando: ')

                    if escolha == '1':
                        periodos = Periodo.listar_periodos()
                        periodo_input = input('Insira o período (de 21.1 a 23.2): ')
                        j=0
                        for periodo in periodos:
                            if periodo.nome == periodo_input:
                                nome_input = input('Insira o nome do professor: ')
                                i=0
                                for professor in periodo.professores:
                                    if professor.nome == nome_input:
                                        professor.avaliar_professor(nome_input)
                                        i+=1
                                if i == 0:
                                    print('Professor não encontrado')
                            j+=1
                        periodo.salvar_periodos(periodos)
                        if j == 0:
                            print('Periodo não encontrado')

                    if escolha == '2':
                        periodos = Periodo.listar_periodos()
                        periodo_input = input('Insira o período (de 21.1 a 23.2): ')
                        j=0
                        for periodo in periodos:
                            if periodo.nome == periodo_input:
                                nome_input = input('Insira o nome do professor: ')
                                i=0
                                for professor in periodo.professores:
                                    if professor.nome == nome_input:
                                        professor.comentar_professor(nome_input,nome_de_usuario)
                                        periodo.salvar_periodos(periodos)
                                        i+=1
                            
                                if i == 0:
                                    print('Professor não encontrado')
                        
                            j+=1

                        if j == 0:
                            print('Periodo não encontrado')

                    if escolha =='3':
                        periodo_input = input('Insira o período (de 21.1 a 23.2): ')
                        Periodo.visualizar_professores(periodo_input)

                    if escolha =='4':
                        j += 1      

        if opcao == '3':
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
