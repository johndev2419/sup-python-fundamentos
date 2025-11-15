from datetime import date
import os
import platform
from rich.align import Align
import questionary
from rich.table import Table
from rich.console import Console
from typing import List

# class Endereco:
#     def __init__(self):
#         self.cidade: str = None
#         self.pais: str = None



# class Desenvolvedora:
#     def __init__(self):
#         self.nome: str = None
#         self.sede: Endereco = None
#         self.proprietario: str = None
#         self.jogos: List[jogo] = []



# # Classe é uma representação de objetos do mundo real
# class jogo:
#     def __init__(self):
#         # prioridades da classe
#         self.titulo: str = None
#         self.data_lancamento: date  = None
#         self.preco: float  = None
#         self.genero: str  = None
#         self.classificacao: str  = None
#         self.desenvolvedora: Desenvolvedora = None

# def exemplo01():
#     Endereco_rockstar = Endereco()
#     Endereco_rockstar.cidade = "New York"
#     Endereco_rockstar.pais = "US"

#     rockstar_games = Desenvolvedora()
#     rockstar_games.nome = "Rockstar Games"
#     rockstar_games.proprietario = "Take-TWO" 
#     rockstar_games.sede = Endereco_rockstar






#     # Instanciando um objeto chamdo gta_vi da classe da classe jogo
#     gta_vi = jogo() # nome_objetos = Nomeclasse()
#     # Definido valor para as propriedades do objetos
#     gta_vi.titulo = "GTA VI"
#     gta_vi.data_lancamento = date(2077, 2, 28)
#     gta_vi.preco = 650
#     gta_vi.genero = "ação"
#     gta_vi.classificacao = "M"

#     gta_vi.desenvolvedora = rockstar_games

#     gta_vi.preco = 669.99

#     the_whitcher = jogo()
#     the_whitcher.titulo = "the witcher 4"
#     the_whitcher.data_lancamento = date(2027, 12, 31)
#     the_whitcher.preco = 500
#     the_whitcher.genero = "RPG"
#     the_whitcher.classificacao = "M"


#     lol = jogo()
#     lol.titulo = "league of lengends"
#     lol.data_lancamento = (2009, 10 , 27)
#     lol.preco = 0
#     lol.genero = "Moba"
#     lol.classificacao = "12"


#     # Adicionar os jogos na desenvolvedora
#     rockstar_games.jogos.append(gta_vi)
#     rockstar_games.jogos.append(the_whitcher)
#     rockstar_games.jogos.append(lol)


#     colunas= ["Desenvolvedora","Titulo", "Data de lançamento", "Preço", "Gênero", "Classificação"]
#     # iNSTACIANDO um objeto chmado tabela da clsse Table
#     tabela= Table(*colunas)

#     tabela.add_row(
#         gta_vi.desenvolvedora.nome,gta_vi.titulo, str(gta_vi.data_lancamento), str(gta_vi.preco), gta_vi.genero,gta_vi.classificacao
#     )
#     tabela.add_row(
#             "N/A", the_whitcher.titulo, str(the_whitcher.data_lancamento), str(the_whitcher.preco), the_whitcher.genero,the_whitcher.classificacao
#     )
#     tabela.add_row(
#             "N/A", lol.titulo, str(lol.data_lancamento), str(lol.preco), lol.genero,lol.classificacao
#     )

#     # instanciando um objeto chamando console de classe console
#     # console = Console()
#     # console.print(tabela)




#     # titulo = "GTA VI"
#     # data_lancamento = date(2077, 2, 28)
#     # preco = 650

#     # gta_vi_dict = {
#     #     "titulo": "GTA VI",
#     #     "data_nascimento": "date(2077,2,28)",
#     #     "preco": "650"
#     # }


# # exercico Criar uma classe chmada Marca  COM  as seguintes atributo :
#  # nome
# #  id(1,2,3,4,5)
# #  fundador str
# #  data de fundação
# #  faturamento float 
# # criar uma função 'execicio_marca'
# # instaciar 2 objetos da classe marca, atribuindo valor para
# # exemplos batatinha = produto()
# #batatinha.valor = 1.30

# class Marca:
#     def __init__(self):
#         self.id: int = None
#         self.nome: str = None
#         self.fundador: str = None
#         self.data_fundacao: date = None
#         self.faturamento: float = None


# def exercicio_marca():
#     shop_ginger = Marca()
#     shop_ginger.id = 1
#     shop_ginger.nome = "Shop Ginger"
#     shop_ginger.fundador = "Marina Ruy Barbosa & Vanessa Ribeiro"
#     shop_ginger.data_fundacao = date(2020, 7, 1)
#     shop_ginger.faturamento =  50_000_000.00

#     alizi = Marca()
#     alizi.id = 2
#     alizi.nome = "Alizi"
#     alizi.fundador = "Marcelo de Castro & Paula J. Castro"
#     alizi.data_fundacao = date(1964, 1, 25)
#     alizi.faturamento = 510_000_000_000.00

#     colunas = ["ID", "NOME", "FUNDADOR", "DATA DE FUNDAÇÃO", "FATURAMENTO"]
#     tabela = Table(*colunas)

#     tabela.add_row(
#         str(shop_ginger.id), shop_ginger.nome, shop_ginger.fundador, str(shop_ginger.data_fundacao), f"{shop_ginger.faturamento}"
#     )
#     tabela.add_row(
#          str(alizi.id), alizi.nome, alizi.fundador, str(alizi.data_fundacao), f"{alizi.faturamento}"
#     )

# #     console = Console()
# #     console.print(tabela)

# # exercicio_marca()

# class Usuario:
#     def __init__(self):
#         self.id: int = None
#         self.nome_completo: str = None
#         self.login: str = None
#         self.data_nascimento: date = None


# class Ticket: 
#     def __init__(self):
#         self.numero: int = None
#         self.usuario: Usuario = None
#         self.data_abertura: date = None
#         self.data_fechamento: date = None
#         self.status: str = None
#         self.descricao: str = None


# def exercicio_ticket():
    
#     usuario1 = Usuario()
#     usuario1.id = 1
#     usuario1.nome_completo = "JOHN LINDO"
#     usuario1.login = "john.gostoso"
#     usuario1.data_nascimento = date(2000, 5, 24)

#     usuario2 = Usuario()
#     usuario2.id = 2
#     usuario2.nome_completo = "Manu Linda"
#     usuario2.login = "manu.lindona"
#     usuario2.data_nascimento = date(1997, 1, 9)

   
#     ticket1 = Ticket()
#     ticket1.numero = 100
#     ticket1.usuario = usuario1
#     ticket1.data_abertura = date.today()
#     ticket1.data_fechamento = date(2025,11,15)
#     ticket1.status = "Em análise"
#     ticket1.descricao = "Erro ao acessar o sistema de relatórios."

#     ticket2 = Ticket()
#     ticket2.numero = 101
#     ticket2.usuario = usuario2
#     ticket2.data_abertura = date.today() 
#     ticket2.data_fechamento = date.today()
#     ticket2.status = "Finalizado"
#     ticket2.descricao = "Solicitação de atualização concluída com sucesso."

   
#     colunas = [
#         "Número",
#         "Usuário",
#         "Login",
#         "Data de Abertura",
#         "Data de Fechamento",
#         "Status",
#         "Descrição",
#     ]
#     tabela = Table(*colunas)

   
#     tabela.add_row(
#         str(ticket1.numero),ticket1.usuario.nome_completo,ticket1.usuario.login,
#         str(ticket1.data_abertura),
#         str(ticket1.data_fechamento),
#         ticket1.status,
#         ticket1.descricao,
#     )

#     tabela.add_row(
#         str(ticket2.numero),ticket2.usuario.nome_completo, ticket2.usuario.login,
#         str(ticket2.data_abertura),
#         str(ticket2.data_fechamento),
#         ticket2.status,
#         ticket2.descricao,
#     )

    
#     console = Console()
#     console.print(tabela)

# exercicio_ticket()




# def limpar_tela():
#     sistema = platform.system()
#     if sistema == "windows":
#         os.system("cls")
#     else:
#         os.system("clear")


# console= Console()
# desenvolvedoras: List[Desenvolvedora] = []


# def menu_sistema():
#     menu_geral =""
#     while menu_geral != "sair":
#         menu_geral = questionary.select("escolha o sistema", choices=["Desenvolvedora","sair"]).ask().lower()
#         limpar_tela()
#         if menu_geral == "desenvolvedora":
#             exemplo_crud_lista_objetos()


# def exemplo_crud_lista_objetos():
#     menu = ""
#     while menu != "sair":
#         menu = questionary.select("Escolha o menu", choices=["Adicionar", "Listar", "Sair"]).ask().lower()
#         limpar_tela()
#         if menu == "adicionar":
#             adicionar_desenvolvedora()
#         elif menu == "listar":
#             lista_desenvolvedora()



# def adicionar_desenvolvedora():
#  # Solicitar os dados, instanciando um objetos de desenvolvedora e adicionar na lista
#    console.print(Align.center("Cadastro de desenvolvedora").style=="blue")   

#    desenvolvedora = Desenvolvedora()
#    desenvolvedora.nome = questionary.text("digite  nome da desenvolvedora").ask()
#    desenvolvedora.proprietario = questionary.text("digite o nome do proprietario").ask()

#    desenvolvedora.sede = Endereco()
#    desenvolvedora.sede.cidade = questionary.text("digite a cidade da sede").ask()
#    desenvolvedora.sede.pais = questionary.text("digite o pais da sede").ask()

#    desenvolvedoras.append(desenvolvedora)
#    console.print("Desenvolvedora cadastrada com sucesso", style="green")
#    input("Pressione ENTER para continuar...")
#    limpar_tela()

# def editar_desenvolvedora():
#     pass 


# def apagar_desenvolvedora():
#     pass # Solicitar a desenvolvedora para apagar e remover da lista


# def lista_desenvolvedora():
#  # Listar desenvolvedoras
#  if len(desenvolvedoras) == 0:
#      console.print("Nenhuma desenvolvedora cadastrada", style="red")
#      input("Pressione ENTER para continuar...")
#      limpar_tela()
#      return
 
#  table = Table("Nome", "Proprietario", "Endereço")

#  for i in range(0, len(desenvolvedoras)):
#         desenvolvedora = desenvolvedoras[i]
#         table.add_row(
#             desenvolvedora.nome,
#             desenvolvedora.proprietario,
#             f"{desenvolvedora.sede.pais} - {desenvolvedora.sede.cidade}"
#         )
    
    
#  console.print(table)

# exemplo_crud_lista_objetos()



# print com ritch do python  e cores


# Criar  um crud de animal e seu dono
# criar uma classe chamada dono comos sequintes atributos abaixo:
 # - nome 
 # - cpf
# criar uma classe chamada animal comos seguintes  atributos abaixos:
# - Raça
# - Dono
# - Data de Nascimento
# Fazer o CR(Create/Read) do Animal solicitando os dados de seu dono também



class Dono:
    def __init__(self):
       self.nome: str = None
       self.cpf: str =  None
       self.bairro: str = None
       self.rua: str =  None
       self.numero : int = None


class Animal:
    def __init__(self):
        self.raca: str = None
        self.nascimento: date = None  
        self.dono: Dono = None
        self.peso: int = None
        self.altura: float = None
        self.sexo: str = None
        self.cor: str = None
        self.origem_raca: str = None


def limpar_tela():
    sistema = platform.system()
    if sistema == "windows":
        os.system("cls")
    else:
        os.system("clear")


console = Console()
animais : List[Animal] = []
donos : List[Dono] = []

def menu_sistema():
    menu_geral = ""
    while menu_geral != "sair" :
        menu_geral = questionary.select(
          "escolha o sistema",
          choices=["Dono","Animal", "Sair"]
        ).ask().lower()
        limpar_tela()
        if menu_geral == "dono":
            crud_dono()
        elif menu_geral == "animal":
            crud_animal()


def crud_dono():
    menu = ""
    while menu != "sair" :
        menu = questionary.select(
            "Menu dono",
            choices=["Adicionar","Listar","Sair"]
        ).ask().lower()
        limpar_tela()

        if menu == "adicionar" :
            adicionar_dono()
        elif menu == "listar":
            listar_donos()


def adicionar_dono():
    console.print(Align.center("Cadastro do Dono"), style="blue")

    dono = Dono()
    dono.nome = questionary.text("Digite o nome do dono: ").ask()
    dono.cpf = questionary.text("Digite o cpf do dono: ").ask()
    dono.bairro = questionary.text("Digite o bairro:").ask()
    dono.rua = questionary.text("Digite a rua:").ask()
    dono.numero = questionary.text("Digite o número:").ask()

    donos.append(dono)

    console.print("Dono cadastrado com sucesso !", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def listar_donos() :

    if len(donos) == 0 :
        console.print("Nenhum dono cadastrado.",style="red")
        input("Pressione ENTER para continuar ...")
        limpar_tela()
        return
    
    tabela = Table("Nome", "CPF")

    for d in donos : 
        tabela.add_row(d.nome, d.cpf,d.bairro,d.rua,d.numero)
    console.print(tabela)

    input("Pressione  ENTER para continuar ...")
    limpar_tela()

def crud_animal():
    menu = ""
    while menu != "sair":
        menu = questionary.select(
            "Menu Animal",
            choices=["Adicionar", "Listar", "Sair"]
        ).ask().lower()

        limpar_tela()

        if menu == "adicionar":
            adicionar_animal()
        elif menu == "listar":
            listar_animais()

def adicionar_animal():

    if len(donos) == 0:
        console.print("Não é possível cadastrar um animal sem cadastrar donos antes.", style="red")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return

    console.print(Align.center("Cadastro de Animal"), style="blue")

    animal = Animal()

    animal.raca = questionary.text("Digite a raça do animal:").ask()
    animal.nascimento = questionary.text("Digite a data de nascimento:").ask()
    animal.peso = questionary.text("Digite o peso do animal:").ask()
    animal.altura = questionary.text("Digite a altura do animal:").ask()
    animal.sexo = questionary.select("Sexo do animal:", choices=["Macho", "Fêmea"]).ask()
    animal.cor = questionary.text("Digite a cor do animal:").ask()
    animal.origem_raca = questionary.text("Digite a origem da raça:").ask()


    
    nomes_donos = [f"{i} - {donos[i].nome}" for i in range(len(donos))]

    indice_escolhido = questionary.select(
        "Escolha o dono do animal:",
        choices=nomes_donos
    ).ask()

    indice = int(indice_escolhido.split(" - ")[0])
    animal.dono = donos[indice]

    animais.append(animal)

    console.print("Animal cadastrado com sucesso!", style="green")
    input("Pressione ENTER para continuar...")
    limpar_tela()

def listar_animais():

    if len(animais) == 0:
        console.print("Nenhum animal cadastrado.", style="red")
        input("Pressione ENTER para continuar...")
        limpar_tela()
        return

    tabela = Table( "Raça", "Nascimento", "Peso", "Altura", "Sexo",
        "Cor", "Origem da Raça", "Dono", "CPF")

    for animal in animais:
        tabela.add_row(
           animal.raca,
            animal.nascimento,
            animal.peso,
            animal.altura,
            animal.sexo,
            animal.cor,
            animal.origem_raca,
            animal.dono.nome,
            animal.dono.cpf
        )

    console.print(tabela)

    input("Pressione ENTER para continuar...")
    limpar_tela()


menu_sistema()





