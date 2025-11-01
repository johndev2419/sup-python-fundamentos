def solicitar_cotacao_dolar() -> float:
    cotacao : float = float(input("Digite o valor da catação do dolar hoje: ").replace(",","."))
    print(cotacao)
    return cotacao

def solicitar_nome_produto() -> str:
    nome = input("Digite o nome do produto: ")
    return nome


def solicitar_valor_produto_dolar() -> float:
    valor_produto_dolar = float( input("digite o valor do produto em dolar: "))
    return valor_produto_dolar


def solicitar_se_pagara_imposto() -> bool:
    pagara_imposto : str = input("pagará imposto (s/n): ").strip().lower()
    if pagara_imposto == "s" :
        return True
    else:
        return False


def solicitar_deseja_ultilizar_cota_mensal() -> bool:
    ultilizar_cota_mensal: str= input("ultilizará a cota mensal (s/n): ").strip().lower()
    if ultilizar_cota_mensal == "s" :
        return True
    else:
        return False
    

def calcular_valor_produto_acrescentando_imposto_utilizando_cota(
        valor_produto_dolar: float,
        cotacao_dolar: float,
        valor_produto_reais: float,
):
    cotacao_mensal = 500.00
    valor_imposto_dolar = (valor_produto_dolar - cotacao_mensal) /2 
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"""
         valor total do prouto: $ {valor_imposto_dolar}
         valor total do produto: R$ {valor_produto_reais}
         valor imposto: R$ {valor_imposto_reais}

        valor total do produto com imposto: R$ {valor_total_produto_reais}""")


def calcular_valor_produto_acrescentando_imposto(
        valor_produto_dolar: float,
        cotacao_dolar: float,
        valor_produto_reais: float,
):
     
    valor_imposto_dolar = valor_produto_dolar /2 
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print("valor total do produto com imposto: " + str(valor_total_produto_reais))


def calcular_valor_compra_paraguai():
    cotacao_dolar: float = solicitar_cotacao_dolar() 
    nome_produto: str = solicitar_nome_produto()
    valor_produto_dolar: float = solicitar_valor_produto_dolar()
    pagara_imposto: bool = solicitar_se_pagara_imposto()
    valor_produto_reais = valor_produto_dolar * cotacao_dolar


    if pagara_imposto == True:
        ultilizar_cota_dolar_mensal = solicitar_deseja_ultilizar_cota_mensal()

        if ultilizar_cota_dolar_mensal == True:
            calcular_valor_produto_acrescentando_imposto_utilizando_cota(
                  valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
        else:
            calcular_valor_produto_acrescentando_imposto(
                 valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
    else:
        print("Valor do produto sem pagar imposto: " + str(valor_produto_reais))

