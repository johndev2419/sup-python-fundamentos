from typing import List


class Aluno :
    def __init__(
        self, nome : str, 
        notas: List[float], 
        frequencia: float = 75, 
        turma: str= "superDEV",
    ):
        self.nome = nome
        self.notas = notas
        self.frequencia = frequencia
        self.turma = turma


def exemplo_passagem_parametros_nomeados():
       # SEGUE POR ORDEM E TERA UM DEFAULT 75%
       #paramentro de frequencia
       # 2 PARAMENTROS SEGUINDO A ORDEM do construtor e outro o valor default nome(turma)
    pedro = Aluno("Pedro silva", [8,7,6.5], turma="superdev o melhor de todos")
       

       # Passando todos os parâmetros pelo nome, podendo passar qualquer ordem
    
    maria = Aluno(
        notas=[10,9.5,10],
        nome="Maria",
        turma="Adas",
        frequencia=100,
    )