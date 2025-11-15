from rich.table import Table
from rich.console import Console
from typing import List


def slavar(nome: str) -> str:
    pass

class cachorro : 
    # Construtor 
    def __init__(self, raca_param: str, peso: float,idade: int, cor: str = "caramelo"):
        # Atributos são preenchidos com os dados dos parâmetros
        # o parametro cor tem um valor default(padrão) que é "caramelo"
        self.raca = raca_param
        self.peso= peso
        self.idade = idade
        self.cor = cor
        # Atributo com dados já pré-definido
        self.cidade_natal = "Blumenau"



def exemlo_construtor_cachorro():
    #cachorro(raca,peso,idade)
    tobby = cachorro("dobberman", 45.20, 15, "preto")
    print("raca: ", tobby.raca)
    print("peso: ", tobby.peso)
    print("idade: ", tobby.idade)
    print("cidade natal: ", tobby.cidade_natal)
    print("cor: ", tobby.cor)

    deschund = cachorro("salsicha", 70.00, 5)
    print("raca: ", deschund.raca)
    print("peso: ", deschund.peso)
    print("idade: ", deschund.idade)
    print("cidade natal: ", deschund.cidade_natal)
    print("cor: ", deschund.cor)



# -------------------------------------------------------------------------------------------
# Criar uma classe chamada passagem com um construtor que contenha os parâmetros abaixos :
# - destino 
# - quantidade dias
#   - data inicio
#  instaciar dois objetos para destinos diferentes, preenchendo os parâmetros
#  apresentar os dados em ua tabela
#  adicionar os parramentros abaixo no construtor da classe passagem 
#   - quantidade pessoas com valor default 2 
#   - partida com valor default 'são paulo'
# instanciar outro objeto passando : destino,  data inicio, quantidade pessoas, partida
# Apresentar na tabela tbm o novo objeto



class Passagem :
    def __init__(self, destino: str, quantidade_dias: int, data_inicio: str,
                 quantidade_pessoas: int = 2, partida: str = "são Paulo"):
        
        self.destino = destino
        self.quantidade_dias = quantidade_dias
        self.data_inicio = data_inicio
        self.quantidade_pessoas = quantidade_pessoas
        self.partida = partida


def exemplos_construtor_passagem() :

    p1 = Passagem("Rio de janeiro", 5, "10/12/2025")
    p2 = Passagem("Salvador", 7, "15/12/2025")
    p3 = Passagem("Curitiba", 4, "20/12/2025", 3)
    p4= Passagem("Fortaleza", 10, "05/01/2026", 5,"campinas")

 
    passagens: List[Passagem] = []

    passagens.append(p1)
    passagens.append(p2)
    passagens.append(p3)
    passagens.append(p4)


console = Console()
table = Table("destino", "quantidades de dias", 
              "data de inicio", "quantidades de pessoas", "partidas")
for p in Passagem :
    table.add_row(
        Passagem.destino,
        str(Passagem.quantidade_dias),
        Passagem.data_inicio,
        str(Passagem.quantidade_pessoas),
        Passagem.partida,
    )
    console.print(table)
  

#     print(f"{'Destino':<15} {'Dias':<6} {'Data início':<15} {'Pessoas':<10} {'Partida':<12}")
#     print("-" * 60)

#     for p in [p1, p2, p3, p4]:
#         print(f"{p.destino:<15} {p.quantidade_dias:<6} {p.data_inicio:<15} {p.quantidade_pessoas:<10} {p.partida:<12}")


exemplos_construtor_passagem() 