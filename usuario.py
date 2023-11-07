from abc import ABC, abstractmethod

class Usuario:
    def __init__(self, nome, id, senha):
        self.nome = nome
        self.id = id
        self.__senha = senha

    def feedback_professor(self):
        pass

    def comentar(self):
        pass

class Administrador(Usuario):
    def __init__(self, nome, id, senha):
        super().__init__(nome, id, senha)

    def adicionar_professor(self):
        pass

    def remover_professor(self):
        pass

    def banir_user(self):
        pass

class User(Usuario):
    def __init__(self, nome, id, senha):
        super().__init__(nome, id, senha)

    def trocar_nome(self):
        pass

    def redefinir_senha(self):
        pass

