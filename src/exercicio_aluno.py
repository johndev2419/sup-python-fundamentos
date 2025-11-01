
# solicitar o nome (criar função)
# solicitar o nota 1 (criar função)
# nota 2 (criar função)
# nota 3 (criar função)
# calcular a media e apresentar 
# criar if que verifique se o aluno está ou não aprovado e apresentar
# solicitar idade (criar função)
# solicitar peso (criar função)
# solicitar altura (criar função)
# calcular o imc do aluno e apresentar a classificação 
# apresentar a geração de acordo com a idade 
# solicitar cargo (criar função)
# apresentar salario de acordo com cargo 
# estagiario R$ 850,00
#  JUNIOR R$ 1800,00
#   PLENO R$ 4000,00
#  SENIOR R$ 6000,00


def solicitar_nota1() -> float:
    nota1 =  float (input("Digite a primeira nota do aluno"))



def solicitar_nome_aluno() -> str:
    nome = str(input("Digite o nome do produto:"))
    return nome 


def verificar_aluno_aprovado_ou_reprovado():
    nome_aluno: str = solicitar_nome_aluno()
    aluno_nota1: float = solicitar_nota1()