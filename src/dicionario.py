from typing import Dict, Union


def exemplo_dicionario_basico():
    # Dicionario é uma forma de armazenar chaves e vlores
    # cada chave esta atrelado a um valor 

    # dicionario tera uma chave do tipo string
    # pode armazenar string, int, ou bool
    # criamos um dicianrio com  2 chaves (apleido, idade)

    cachorro: dict[str, Union[str, int, bool, float]] = {
        "apelido": "Tobby" ,
        "idade" : 4 ,
        "abandonado": True,
        "peso": 22.5
    }

    #acrescentar uuma nova chave com um valor
    cachorro["raca"] = "pastor alemão"

    cachorro["cor"] = "caramelo"

    #alterar o valor de uma chave 
    cachorro["idade"] = 5

    #remover uma chave(automaticamente remove o valor)
    cachorro.pop("abandonado")

    #print("cachorro:" , cachorro["apelido"])
    print(f"""
cachorro: {cachorro.get("apelido")}
raça: {cachorro.get("raca")}
idade: {cachorro.get("idade")}
cor: {cachorro.get("cor")}
abandonado: {cachorro.get("abandonado")}
peso: {cachorro.get("peso")}
""")
    
    #exercicio 01
    # Criar ua função exemplo_dicionario_aluno
    # criar um dicionario chamado aluno com seguintes dados 
     #nome comppleto
     #nome_mae
     #nome_pai
     #jogar(true)
     # apresentar os dados do dicionario
     # adicionar a chave idade do aluno
     #apresentar a idade do aluno
     # alterar a idade do aluno para +1
     # REMOVER  a chave jogar do aluno
     # apresentar os dados 

def exemplo_dicionario_aluno():

    aluno:dict[str,Union[str,bool,int]] = {
      "nome_completo": "João Silva",
      "nome_mae": "Maria Silva",
      "nome_pai": "josé Silva",
      "jogar": True
    }

    print(f"""
     Dados iniciais do aluno: {aluno}
""")
    
    aluno["idade"] = 15
    print("\nIdade do aluno: ", aluno["idade"])

    aluno["idade"] += 1
    print("idade do aluno adicionado ciclo: ", aluno["idade"])

    del aluno["jogar"]

    print("\n Dados atualizados do aluno(sem jogar): ")
    print(aluno)
    