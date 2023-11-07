from abc import ABC, abstractmethod

class Materia:
    def __init__(self, nome, codigo, creditos, professores = []):
        self.nome = nome
        self.codigo = codigo
        self.creditos = creditos
        self.professores = professores

    def adc_professor(self):
        pass

    def rmv_professor(self):
        pass
