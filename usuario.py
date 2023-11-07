from abc import ABC, abstractmethod

class Usuario:
    def __init__(self, nome, senha, nome_de_usuario):
        self._nome = nome
        self.__senha = senha
        self.nome_de_usuario = nome_de_usuario

    def feedback_professor(self):
        pass

    def comentar(self):
        pass

class Administrador(Usuario):
    def __init__(self, nome, senha, nome_de_usuario):
        super().__init__(nome, senha, nome_de_usuario)

    def adicionar_professor(self):
        pass

    def remover_professor(self):
        pass

    def banir_user(self):
        pass

    def user_2_adm(self,user):
        pass

class User(Usuario):
    def __init__(self, nome, senha, nome_de_usuario):
        super().__init__(nome, senha, nome_de_usuario)

    def trocar_nome(self):
        pass

    def redefinir_senha(self):
        pass

