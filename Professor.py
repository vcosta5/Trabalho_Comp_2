from abc import ABC, abstractmethod

class Professor:
    def __init__(self, nome, idade, avaliação, cv_lattes, materias=[]):
        self.nome = nome
        self.idade = idade
        self.avaliação = avaliação
        self.cv_lattes = cv_lattes
        self.materias = materias

    def adc_materia(self):
        pass

    def rmv_materia(self):
        pass
