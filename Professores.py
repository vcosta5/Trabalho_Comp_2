import pickle
from Exceções import RatingError

class Professores:
    def __init__(self,nome, materia):
        self.nome = nome
        self.materia = materia
        self.avaliação = 0
        self.listar_avaliacoes = []
        self.comentarios = []

    @staticmethod
    def cadastrar_professor(nome, materia):
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome:
                return

        novo_professor = Professores(nome,materia)
        professores.append(novo_professor)
        Professores.salvar_professores(professores)
        print(f"Professor {nome} cadastrado com sucesso.")

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
    def avaliar_professor(nome_professor, nome_usuario):
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome_professor:
                comentario = input('Insira seu comentário: ')
                professor.comentarios.append(f'{nome_usuario}: {comentario}')
                i=0
                while i == 0:
                    try:
                        nota = int(input('Insira uma nota de 0 a 5 para esse professor: '))
                        if nota > 5 or nota <0:
                            raise RatingError('Insira uma nota dentro do intervalo estabelecido')
                        professor.listar_avaliacoes.append(nota)
                        i+=1
                    except ValueError:
                        print('Insira um número')
                professor.avaliação = sum(professor.listar_avaliacoes)/len(professor.listar_avaliacoes)
        Professores.salvar_professores(professores)
        print(f"Professor {nome_professor} avaliado com sucesso.")

    @staticmethod
    def salvar_professores(professores):
        with open('professores.pickle', 'wb') as file:
            pickle.dump(professores, file)


