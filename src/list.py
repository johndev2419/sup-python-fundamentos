from typing import List


def exemplo_lista_basica():
    #criando uma lista de string e armazenando um nome
    nomes: List[str] = ["João"]

    #acrescentar item na lista
    nomes.append("Maria")

    #obter o nome d posição zero 
    nome_primeira_posição = nomes[0]

    #alterar o nome do joão que está na primeira posição
    nomes[0] = "João cleber"

    #adicionar elemento para depois apagar
    nomes.append("lúcio")

    #APAGAR UM ELEMENTO DA LISTA    
    nomes.remove("lúcio")

    tamanho_lista = len(nomes)

    print(f""" primeiro nome: {nomes[0]}
       segundo nome: {nomes[1]}
       tamanho da lista: {tamanho_lista}
          """)
    
    
def exemplo_solictar_dados_usuario():
        valores = []

        valores.append(float(input("Digite os valores: ")))
        valores.append(float(input("Digite os valores: ")))
        valores.append(float(input("Digite os valores: ")))
        valores.append(float(input("Digite os valores: ")))
        valores.append(float(input("Digite os valores: ")))

        soma = valores[0] + valores[1] + valores[2] + valores[3] + valores[4]

        print(valores)
        print(soma)


def exemplo_solictar_dados_usuario_otimizado():
    valores = []


    for i in range(0, 5):
       valores.append(float(input("Digite os valores: ")))

    soma = 0
    for i in range(0, 5):
       valor = valores[i]
       soma = soma + valor
    print(f"""soma: {soma}""")


def exemplo_lista_com_dicionario():
    #pip install --requirement requirements.txt
    


    