from Exceções import TimMaiaError, LoginEmptyError, LoginPasswordError, LoginUserError
from Professores import Professores
from Materia import Materia
from Periodo import Periodo
import pickle

class BancoDeDados:

    def criar_materias():
        Materia.cadastrar_materia("Física 1","FIT112")
        Materia.cadastrar_materia("Física 2","FIT122")
        Materia.cadastrar_materia("Física 3","FIM230")
        Materia.cadastrar_materia("Física 4","EEU240")
        Materia.cadastrar_materia("Cálculo 1","MAC118")
        Materia.cadastrar_materia("Cálculo 2","MAC128")
        Materia.cadastrar_materia("Cálculo 3","MAC238")
        Materia.cadastrar_materia("Cálculo 4","MAC248")
        Materia.cadastrar_materia("Computação 1","ICP114")
        Materia.cadastrar_materia("Computação 2","ICP225")

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
        Professores.cadastrar_professor('Cafu','Cálculo 3')
        Professores.cadastrar_professor('Sara','Cálculo 3')
        Professores.cadastrar_professor('Alan','Cálculo 4')
        Professores.cadastrar_professor('Ricardo','Cálculo 4')
        Professores.cadastrar_professor('Bruna','Computação 1')
        Professores.cadastrar_professor('Isabela','Computação 1')
        Professores.cadastrar_professor('Luiz Paulo','Computação 2')
        Professores.cadastrar_professor('Careca','Computação 2')

    @staticmethod
    def criar_periodos():
        Periodo.cadastrar_periodo('21.1')
        Periodo.cadastrar_periodo('21.2')
        Periodo.cadastrar_periodo('22.1')
        Periodo.cadastrar_periodo('22.2')
        Periodo.cadastrar_periodo('23.1')
        Periodo.cadastrar_periodo('23.2')

    def listas_periodos():
        periodos = Periodo.listar_periodos()
        for periodo in periodos:
            periodo.materias = Materia.listar_materias()
            periodo.professores = Professores.listar_professores()
        Periodo.salvar_periodos(periodos)
