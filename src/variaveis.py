def exemplo_strings():
    nome_inquilino: str = "maria"
    sobrenome_inquilino : str = "jão"

    nome_completo : str = nome_inquilino + " " + sobrenome_inquilino
    print(nome_completo)


def apresentar_dados_pacientes():

        nome_paciente : str = "João" 

        cidade_natal: str = "Aracaju"
        tipo_sanguineo: str = "A"
        apresentar_tudo: str = nome_paciente + " " + cidade_natal + " " + tipo_sanguineo
        print(apresentar_tudo)

def apresentar_dados_complemetares():
      idade_paciente : int = 25
      peso_paciente : float = 73.3
      altura_paciente : float = 1.73

      calcular_imc : float = peso_paciente / (altura_paciente * peso_paciente)

      from datetime import date
      ano_atual = date.today().year
      ano_nascimento = ano_atual - idade_paciente

      print("\n Seu imc:" + str(calcular_imc))
      print("Você nasceu em" + str(ano_nascimento))

def exemplo_boolean():
      # boolean: true(verdadeiro) ou false(falso)
      empregado: bool = True
      # Alterando o valor da variável empregado
      empregado = False

      print("Empregado: " + str(empregado))

def funcao_sem_retorno():
    print("Ola Mundo")

def funcao_com_retorno() -> str:
      produto : str = "iphone laranja"
      return produto

def funcao_executar():
      funcao_sem_retorno()

      nome = funcao_com_retorno()
      print("nome do produto: " + nome)

