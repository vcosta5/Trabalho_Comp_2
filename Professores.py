import pickle
from Exceções import RatingError, CommentError
from Materia import Materia

class Professores:
    def __init__(self,nome, materia):
        self.nome = nome
        self.materia = materia
        self.avaliações = 0
        self.didática = 0
        self.organizacao = 0
        self.lista_avaliações = []
        self.lista_didatica = []
        self.lista_organizacao = []
        self.comentarios = []

    @staticmethod
    def cadastrar_professor(nome, nome_materia):
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome:
                return

        novo_professor = Professores(nome, nome_materia)
        professores.append(novo_professor)
        Professores.salvar_professores(professores)

        materias = Materia.listar_materias()
        for materia in materias:
            if materia.nome == nome_materia:
                materia.professores.append(novo_professor)
        Materia.salvar_materias(materias)

    @staticmethod
    def consultar_professor_nome(nome):
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome:
                return professor
        return None
    
    @staticmethod
    def consultar_professor_materia(materia):
        lista_professores = []
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.materia == materia:
                lista_professores.append(professor)              
        return lista_professores

    @staticmethod
    def listar_professores():
        try:
            with open('professores.pickle', 'rb') as file:
                professores = pickle.load(file)
        except (FileNotFoundError, EOFError):
            professores = []
        return professores

    @staticmethod
    def avaliar_professor(nome_professor):
        palavras_proibidas = ['morte','morrer','matar','etc']
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome_professor:
                i=0
                while i == 0:
                    try:
                        avaliacoes = int(input(f'Dê uma nota para as avaliações de {professor.nome}(de 0 a 5): '))
                        didatica = int(input(f'Dê uma nota para a didática de {professor.nome}(de 0 a 5): '))
                        organizacao = int(input(f'Dê uma nota para a organização de {professor.nome}(de 0 a 5): '))

                        #nota = int(input('Insira uma nota de 0 a 5 para esse professor: '))
                        #if nota > 5 or nota <0:
                        #    raise RatingError('Insira uma nota dentro do intervalo estabelecido')

                        professor.lista_avaliações.append(avaliacoes)
                        professor.lista_didatica.append(didatica)
                        professor.lista_organizacao.append(organizacao)
                        professor.avaliações = sum(professor.lista_avaliações)/len(professor.lista_avaliações)
                        professor.didática = sum(professor.lista_didatica)/len(professor.lista_didatica)
                        professor.organizacao = sum(professor.lista_organizacao)/len(professor.lista_organizacao)
                        i+=1
                    except ValueError:
                        print('Insira um número')
                    Professores.salvar_professores(professores)
        print(f"Professor {nome_professor} avaliado com sucesso.")

    @staticmethod
    def comentar_professor(nome_professor,nome_usuario):
        palavras_proibidas = ['morte','morrer','matar','etc']
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome_professor:
                try:
                    comentario = input('Insira seu comentário: ')
                    for palavra in palavras_proibidas:
                        if palavra in comentario:
                            raise CommentError
                    professor.comentarios.append(f'{nome_usuario}: {comentario}')
                except CommentError:
                    print('comentário bloqueado')
        Professores.salvar_professores(professores)
        
    @staticmethod
    def salvar_professores(professores):
        with open('professores.pickle', 'wb') as file:
            pickle.dump(professores, file)
