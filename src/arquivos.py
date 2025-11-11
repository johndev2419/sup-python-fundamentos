from typing import List
from json import dumps,load
from pathlib import Path

#import json
# json.dumps()


def escrever_json(data: List, nome_arquivo: str):
   caminho = Path(nome_arquivo).resolve()
#    converte um objeto em python para uma string json 
   json_string: str =  dumps(data, ensure_ascii=False)
   with open(caminho, mode="w", encoding="utf-8") as arquivo:
     arquivo.write(json_string)
     arquivo.flush()

def ler_json(nome_arquivo: str) -> List | dict :
 caminho = Path(nome_arquivo).resolve()
 
 with open(caminho, mode="r", encoding="utf-8") as arquivo:
   dado_desrializado = load(arquivo)
   return dado_desrializado
 

def exemplos_criar_arquivos() :
  produtos = [
    {
      "nome": "abacate",
      "preco": 25.00
    },
    {
      "nome": "banana",
      "preco": 4.50
    },
    {
      "nome": "uva",
      "preco": 6.70
    }
  ]

  escrever_json(produtos,"produtos.json")

  games = ["minecraft", "roblox", "cs"]
  escrever_json(games,"games.json")

  mine = {
    "nome" : "minecraft",
    "classificacao": 18,
    "preco": 350.00
  }
  escrever_json(mine,"mine.json")

# exemplos_criar_arquivos()


# produtos = ler_json("produtos.json")
# games = ler_json("games.json")
# mine = ler_json("mine.json")


# print(produtos[2].get("nome"))
# print(games[0])
# print(mine.get("nome"))

