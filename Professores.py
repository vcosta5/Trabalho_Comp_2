import pickle
from Exceções import RatingError, CommentError
from Materia import Materia

class Professores:
    def __init__(self,nome, materia):
        self.nome = nome
        self.materia = materia
        self.avaliação = 0
        self.listar_avaliacoes = []
        self.comentarios = []

    @staticmethod 
    '''Staticmethod: Um método estático dentro de uma classe indica que este método pode ser invocado sem a necessidade de que você tenha uma instância desta classe. '''
  
    def cadastrar_professor(nome, nome_materia): '''tem a função de cadastrar os professores e listar eles '''
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome:
                return

''' O append é para quando você quer adicionar um único item em uma lista. Será adicionado um novo professor e salvo'''
  
        novo_professor = Professores(nome, nome_materia)
        professores.append(novo_professor)
        Professores.salvar_professores(professores)

''' listar.materias retorna uma lista e a partir disso se roda o "For".'''
        
        materias = Materia.listar_materias()
        for materia in materias:
            if materia.nome == nome_materia:
                materia.professores.append(novo_professor)
        Materia.salvar_materias(materias)

    @staticmethod
''' Se o nome do professor estiver no atributo 'nome', retorna o nome do professor, caso não esteja, retorna nada.'''
    def consultar_professor_nome(nome):
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome:
                return professor
        return None
    
    @staticmethod
''' Consulta, na lista de professores, a matéria do professor e se tem mais de um professor para cada matéria '''
    
    def consultar_professor_materia(materia): '''Método que consulta os professores de cada matéria'''
        lista_professores = []
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.materia == materia:
                lista_professores.append(professor)              
        return lista_professores

'''pickle mantém o controle dos objetos que já serializou, para que referências posteriores ao mesmo objeto não sejam serializadas novamente.'''
    @staticmethod
    def listar_professores(): ''' Método que lista os professores, busca na classe professores e lê apenas esse arquivo'''
        try:
            with open('professores.pickle', 'rb') as file: '''quando se passa rb como paramentro, ele lê apenas o arquivo'''
                professores = pickle.load(file)
        except (FileNotFoundError, EOFError):
            professores = []
        return professores

    @staticmethod
    def avaliar_professor(nome_professor): '''Método para avaliar os professores. Pede-se que avalie o professor com uma nota de 0 a 5, caso a nota for maior que 5 ou menor qe zero, ou seja, não esteja nesse intervalo, é pedido para o aluno que avalie com um número do intervalo estabelecido. 
    O número não pode ser escrito, o numéro tem que ser um algarismo. Depois de salvar, é esperado uma mensagem avisando que o professor escolhido foi avaliado com sucesso'''
        palavras_proibidas = ['morte','morrer','matar','etc']
        professores = Professores.listar_professores()
        for professor in professores:
            if professor.nome == nome_professor:
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
    def comentar_professor(nome_professor,nome_usuario): '''Método para adicionar um comentário para o professor que desejar, exeto comentarios com palavras proibidas, pois essas serão bloqueadas.'''
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

    @staticmethod
    def salvar_professores(professores):
        with open('professores.pickle', 'wb') as file:
            pickle.dump(professores, file)


