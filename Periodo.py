from Professores import Professores
from Materia import Materia
import pickle

class Periodo: 
    def __init__(self,nome):
        self.nome = nome
        self.professores = []
        self.materias = []


    def visualizar_materias(periodo_input):
        periodos = Periodo.listar_periodos()
        for periodo in periodos:
            if periodo.nome == periodo_input:
                for materia in periodo.materias:
                    print(f'Matéria: {materia.nome} | Código: {materia.codigo}')
                    print(f'Avaliações: {materia.avaliacoes} \nDificuldade: {materia.dificuldade} \nEmenta: {materia.ementa} \nSuporte: {materia.suporte}')
                    for comentario in materia.comentarios:
                        print(f'{comentario}')

    def visualizar_professores(periodo_input):
        periodos = Periodo.listar_periodos()
        for periodo in periodos:
            if periodo.nome == periodo_input:
                for professor in periodo.professores:
                    print(f'Professor: {professor.nome} | Código: {professor.materia}')
                    print(f'Avaliações: {professor.avaliações} \nDidática: {professor.didática} \nOrganização: {professor.organizacao}')
                    for comentario in professor.comentarios:
                        print(f'{comentario}')
            

    @staticmethod
    def cadastrar_periodo(nome):
        periodos = Periodo.listar_periodos()
        for periodo in periodos:
            if periodo.nome == nome:
                return
            
        novo_periodo = Periodo(nome)
        periodos.append(novo_periodo)
        Periodo.salvar_periodos(periodos)

        print(f"Período {nome} cadastrado com sucesso.")

    @staticmethod
    def listar_periodos():
        try:
            with open('periodos.pickle', 'rb') as file:
                periodos = pickle.load(file)
        except (FileNotFoundError, EOFError):
            periodos = []
        return periodos

    @staticmethod
    def salvar_periodos(periodos):
        with open('periodos.pickle', 'wb') as file:
            pickle.dump(periodos, file)
