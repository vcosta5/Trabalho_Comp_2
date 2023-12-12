import pickle

class Materia:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.lista_avaliacoes = []
        self.lista_dificuldade = []
        self.lista_ementa = []
        self.lista_suporte = []
        self.comentarios = []
        self.professores = []
        self.avaliacoes = 0
        self.dificuldade = 0
        self.ementa = 0
        self.suporte = 0

    @staticmethod
    def visualizar_materias(lista):
        for materia in lista:
            print(f'Matéria: {materia.nome} | Código: {materia.codigo}')
            print(f'Avaliações: {materia.avaliacoes} \nDificuldade: {materia.dificuldade} \nEmenta: {materia.ementa} \nSuporte: {materia.suporte}')

    @staticmethod
    def cadastrar_materia(nome_materia, codigo):
        materias = Materia.listar_materias()
        for materia in materias:
            if materia.nome == nome_materia or materia.codigo == codigo:
                return

        nova_materia = Materia(nome_materia, codigo)
        materias.append(nova_materia)
        Materia.salvar_materias(materias)

        print(f"Matéria {nome_materia} cadastrada com sucesso.")

    @staticmethod
    def listar_materias():
        try:
            with open('materias.pickle', 'rb') as file:
                materias = pickle.load(file)
        except (FileNotFoundError, EOFError):
            materias = []
        return materias

    @staticmethod
    def salvar_materias(materias):
        with open('materias.pickle', 'wb') as file:
            pickle.dump(materias, file)

    @staticmethod
    def comentar_materia(codigo,nome_de_usuário):
        materias = Materia.listar_materias()
        i = 0
        for materia in materias:
            if materia.codigo == str.upper(codigo):
                comentario = input('Insira seu comentário: ')
                materia.comentarios.append(f'{nome_de_usuário}: {comentario}')
                Materia.salvar_materias(materias)
                i+=1
        if i == 0:
            print('Matéria não cadastrada')


    @staticmethod
    def avaliar_materia(codigo):
        materias = Materia.listar_materias()
        i = 0
        for materia in materias:
            if materia.codigo == str.upper(codigo):
                avaliacoes = int(input(f'Dê uma nota para as avaliações de {materia.nome}(de 0 a 5): '))
                dificuldade = int(input(f'Dê uma nota para a dificuldade de {materia.nome}(de 0 a 5): '))
                ementa = int(input(f'Dê uma nota para a ementa de {materia.nome}(de 0 a 5): '))
                suporte = int(input(f'Dê uma nota para o suporte de {materia.nome}(de 0 a 5): '))
                materia.lista_avaliacoes.append(avaliacoes)
                materia.lista_dificuldade.append(dificuldade)
                materia.lista_ementa.append(ementa)
                materia.lista_suporte.append(suporte)
                materia.avaliacoes = sum(materia.lista_avaliacoes)/len(materia.lista_avaliacoes)
                materia.dificuldade = sum(materia.lista_dificuldade)/len(materia.lista_dificuldade)
                materia.ementa = sum(materia.lista_ementa)/len(materia.lista_ementa)
                materia.suporte = sum(materia.lista_suporte)/len(materia.lista_suporte)
                Materia.salvar_materias(materias)
                i+=1
        if i == 0:
            print('Matéria não cadastrada')

