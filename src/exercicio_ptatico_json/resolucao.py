from typing import Dict, List
from src.arquivos import ler_json, escrever_json
from rich.console import Console
from rich.table import Table

def resolve() : 



   usuarios: List[Dict[str,any]] = ler_json("data/usuarios.json")

   ativos, suspensos, inativos = [], [], []

   for i in range (0, len(usuarios)):
      usuario = usuarios[i]
      conta = usuario.get("conta")
      status= conta.get("status")
      tipo = conta.get("tipo")
      pontuacao = conta.get("pontos")

      assinatura = usuario.get("assinatura",{})
      plano = assinatura.get("plano", "Sem assinatura")

      dados_pessoais = usuario.get("dados_pessoais")
      nome = dados_pessoais.get("nome")
      email = dados_pessoais.get("email")

      dados = {
         "nome": nome,
         "email": email,
         "tipo": tipo,
         "pontos": pontuacao,
         "plano": plano

      }

      if status == "ativo" : 
         #print (nome,"ativo")
         ativos.append(dados)
      elif status == "suspenso" :
         suspensos.append(dados)
      else:
         inativos.append(dados)

   escrever_json(ativos,"data/ativos.json")
   escrever_json(suspensos, "data/suspensos.json")
   escrever_json(inativos, "data/inativos.json")

   apresentar_tabela(ativos, "Contas Ativas")
   apresentar_tabela(inativos, "Contas Inativas")
   apresentar_tabela(suspensos, "Contas Suspenso")

def apresentar_tabela(dados: List[dict[str,str]], titulo: str) :
   table = Table(title=titulo)
   table.add_column("Nome", header_style="magenta")
   table.add_column("E-mail", style="blue")
   table.add_column("Tipo", header_style="green")
   table.add_column("pontuação")
   table.add_column("plano")

   for i in range(0, len(dados)):
      dado = dados[i]
      table.add_row (
         dado.get("nome"),
         dado.get("email"),
         dado.get("tipo"),
         str(dado.get("pontos")),
         dado.get("plano"),
      )

   console = Console()
   console.print(table)




# Exercício 01
#   Percorrer a lista de usuário, armazenando no arquivo 'free.json' o nome dos usuários que tem o plano Free
# Exercício 02
#   Percorrer a lista de usuário, armazenando no arquivo 'tags.json' todas as tags dos usuários
# Exercício 03
#   Percorrer a lista de usuário, armazenando no arquivo 'enderecos.json' todos os endereços dos usuários
# Ex.: ["Rua - Numero - Bairro - CEP - UF", "Rua - Numero - Bairro - CEP - UF"]
# Exercício 04:
#   Percorrer a lista de usuários agrupando os dados por estado, salvando o telefone e e-mail de cada usuário em uma lista por estado. Deve armazenar uma lista com os usuários conforme abaixo:
#   Ex.: sc.json
#       [{"email": "elisa.rocha@example.com", "telefone": "......"}]



def exercicio01():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    ativos, suspensos, inativos = [], [], []
    free_users = []  

    for i in range(len(usuarios)):
        usuario = usuarios[i]
        conta = usuario.get("conta", {})
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontos")

        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "Sem assinatura")

        dados_pessoais = usuario.get("dados_pessoais", {})
        nome = dados_pessoais.get("nome", "Sem nome")
        email = dados_pessoais.get("email", "Sem email")

        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "pontos": pontuacao,
            "plano": plano
        }

       
        if status == "ativo":
            ativos.append(dados)
        elif status == "suspenso":
            suspensos.append(dados)
        else:
            inativos.append(dados)

       
        if plano.lower() == "free":
            free_users.append({"nome": nome})

   
    escrever_json(ativos, "data/ativos.json")
    escrever_json(suspensos, "data/suspensos.json")
    escrever_json(inativos, "data/inativos.json")
    escrever_json(free_users, "data/free.json") 
    
    apresentar_tabela(ativos, "Contas Ativas")
    apresentar_tabela(inativos, "Contas Inativas")
    apresentar_tabela(suspensos, "Contas Suspensas")

def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome", header_style="magenta")
    table.add_column("E-mail", style="blue")
    table.add_column("Tipo", header_style="green")
    table.add_column("Pontuação")
    table.add_column("Plano")

    for dado in dados:
        table.add_row(
            dado.get("nome"),
            dado.get("email"),
            dado.get("tipo"),
            str(dado.get("pontos")),
            dado.get("plano")
        )

    console = Console()
    console.print(table)


def exercicio02():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    ativos, suspensos, inativos = [], [], []
    tags_coletadas = [] 

    for i in range(len(usuarios)):
        usuario = usuarios[i]
        conta = usuario.get("conta", {})
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontos")

        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "Sem assinatura")

        dados_pessoais = usuario.get("dados_pessoais", {})
        nome = dados_pessoais.get("nome", "Sem nome")
        email = dados_pessoais.get("email", "Sem email")

        
        tags_usuario = usuario.get("tags", [])
        if isinstance(tags_usuario, list):
            tags_coletadas.extend(tags_usuario)
        tags_usuario = usuario.get("tags", [])
        if isinstance(tags_usuario, list):
          tags_coletadas.extend(tags_usuario)
          tags_str = ", ".join(tags_usuario)

        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "pontos": pontuacao,
            "plano": plano,
            "tags": tags_str
        }

        
        if status == "ativo":
            ativos.append(dados)
        elif status == "suspenso":
            suspensos.append(dados)
        else:
            inativos.append(dados)

    escrever_json(ativos, "data/ativos.json")
    escrever_json(suspensos, "data/suspensos.json")
    escrever_json(inativos, "data/inativos.json")

 
    tags_unicas = sorted(list(set(tags_coletadas)))
    escrever_json(tags_unicas, "data/tags.json")


    apresentar_tabela(ativos, "Contas Ativas")
    apresentar_tabela(inativos, "Contas Inativas")
    apresentar_tabela(suspensos, "Contas Suspensas")

def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome", header_style="magenta")
    table.add_column("E-mail", style="blue")
    table.add_column("Tipo", header_style="green")
    table.add_column("Pontuação")
    table.add_column("Plano")
    table.add_column("Tags", header_style="cyan")


    for dado in dados:
        table.add_row(
            dado.get("nome",),
            dado.get("email"),
            dado.get("tipo"),
            str(dado.get("pontos")),
            dado.get("plano"),
            dado.get("tags")
        )

    console = Console()
    console.print(table)


def exercicio03():
 
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    ativos, suspensos, inativos = [], [], []
    free_users = []  
    tags_coletadas = []   
    enderecos = []   

    for usuario in usuarios:
        conta = usuario.get("conta", {})
        status = conta.get("status")
        tipo = conta.get("tipo")
        pontuacao = conta.get("pontos")

        assinatura = usuario.get("assinatura", {})
        plano = assinatura.get("plano", "Sem assinatura")

        dados_pessoais = usuario.get("dados_pessoais", {})
        nome = dados_pessoais.get("nome", "Sem nome")
        email = dados_pessoais.get("email", "Sem email")

       
        if plano.lower() == "free":
            free_users.append({"nome": nome})

        
        tags_usuario = usuario.get("tags", [])
        if isinstance(tags_usuario, list):
            tags_coletadas.extend(tags_usuario)
        tags_str = ", ".join(tags_usuario) 

       
        endereco_info = usuario.get("endereco", {})
        if endereco_info:
            rua = endereco_info.get("rua", "")
            numero = endereco_info.get("numero", "")
            bairro = endereco_info.get("bairro", "")
            cep = endereco_info.get("cep", "")
            uf = endereco_info.get("uf", "")
            endereco_formatado = f"{rua} - {numero} - {bairro} - {cep} - {uf}"
            enderecos.append(endereco_formatado)
        else:
            endereco_formatado = ""  

        
        dados = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "pontos": pontuacao,
            "plano": plano,
            "tags": tags_str,
            "endereco": endereco_formatado
        }

      
        if status == "ativo":
            ativos.append(dados)
        elif status == "suspenso":
            suspensos.append(dados)
        else:
            inativos.append(dados)

    escrever_json(ativos, "data/ativos.json")
    escrever_json(suspensos, "data/suspensos.json")
    escrever_json(inativos, "data/inativos.json")
    escrever_json(free_users, "data/free.json")
    escrever_json(tags_coletadas, "data/tags.json")
    escrever_json(enderecos, "data/enderecos.json")

 
    apresentar_tabela(ativos, "Contas Ativas")
    apresentar_tabela(inativos, "Contas Inativas")
    apresentar_tabela(suspensos, "Contas Suspensas")


def apresentar_tabela(dados: List[Dict[str, str]], titulo: str):
    table = Table(title=titulo)
    table.add_column("Nome", header_style="magenta")
    table.add_column("E-mail", style="blue")
    table.add_column("Tipo", header_style="green")
    table.add_column("Pontuação")
    table.add_column("Plano")
    table.add_column("Tags", header_style="cyan")
    table.add_column("Endereço", header_style="yellow")

    for dado in dados:
        table.add_row(
            dado.get("nome", ""),
            dado.get("email", ""),
            dado.get("tipo", ""),
            str(dado.get("pontos", "")),
            dado.get("plano", ""),
            dado.get("tags", ""),
            dado.get("endereco", "")
        )

    console = Console()
    console.print(table)





def exercicio04():
    usuarios: List[Dict[str, any]] = ler_json("data/usuarios.json")

    estados: Dict[str, List[Dict[str, str]]] = {}  

    for usuario in usuarios:
        dados_pessoais = usuario.get("dados_pessoais", {})
        email = dados_pessoais.get("email", "Sem email")
        telefone = dados_pessoais.get("telefone", "Sem telefone")

        endereco_info = usuario.get("endereco", {})
        uf = endereco_info.get("uf", "Sem UF")

        if uf not in estados:
            estados[uf] = []

        estados[uf].append({
            "email": email,
            "telefone": telefone
        })

    
   

    console = Console()

    for uf, lista_usuarios in estados.items():
      
        arquivo_estado = f"data/{uf.lower().replace(' ', '_')}.json"
        escrever_json(lista_usuarios, arquivo_estado)

     
        table = Table(title=f"Usuários do estado {uf}")
        table.add_column("E-mail", style="blue")
        table.add_column("Telefone", style="green")

        for usuario in lista_usuarios:
            table.add_row(
                usuario.get("email", ""),
                usuario.get("telefone", "")
            )

        console.print(table)
        print(f"Arquivo salvo: {arquivo_estado} ({len(lista_usuarios)} usuários)\n")
