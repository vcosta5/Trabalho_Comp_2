from abc import ABC, abstractmethod

class Usuario:
    def __init__(self, nome_de_usuario, senha, nome = ''):
        self._nome = nome
        self.__senha = senha
        self.nome_de_usuario = nome_de_usuario
        self.logado = False

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,nova_senha):
        self.__senha = nova_senha

    def logar(self):
        self.logado = True

    def feedback_professor(self):
        pass

    def comentar(self):
        pass

class Administrador(Usuario):
    def __init__(self, nome_de_usuario, senha, nome = ''):
        super().__init__(nome_de_usuario, senha, nome = '')

    def adicionar_professor(self):
        pass

    def remover_professor(self):
        pass

    def banir_user(self):
        pass

    def user_2_adm(self,user):
        pass

class User(Usuario):
    def __init__(self, nome_de_usuario, senha, nome = ''):
        super().__init__(nome_de_usuario, senha, nome = '')

    def trocar_nome(self):
        pass

    def redefinir_senha(self):
        pass

