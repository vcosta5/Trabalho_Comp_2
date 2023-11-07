class BancoDeDados:
    def __init__(self, lista_usuarios = [], lista_materias = [], lista_professores = []):
        self.lista_usuarios = lista_usuarios
        self.lista_materias = lista_materias
        self.lista_professores = lista_professores

    def adc_usuarios(self, usuario):
        self.lista_usuarios.append(usuario)

    def listar_usuarios(self):
        print('         Lista de usuários         ')
        print('--------------------------------')
        for i in self.lista_usuarios:
            print(f"Nome de usuário: {i.nome_de_usuario}")
        print('--------------------------------')

    
    def listar_materias(self):
        pass

    def listar_professores(self):
        pass
