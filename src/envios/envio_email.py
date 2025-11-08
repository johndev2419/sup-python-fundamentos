from dotenv import load_dotenv
from os import getenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# carregar as variáveis de dentro do arquivo .env para as variaveis do ambientes
load_dotenv()

def __obter_login() -> str:
    email = getenv("EMAIL")
    if email is None:
        raise Exception("login não esta preenchido no arquivo .env")
    
    return email

def __obter_senha() -> str:
    senha = getenv("senha")
    if senha is None:
        raise Exception("senha nao esta preenchida no arquivo .env")
    
    return senha

def enviar(destinatario: str, corpo: str):
    mensagem = MIMEMultipart()
    mensagem["From"] = __obter_login()
    mensagem["To"] = destinatario
    mensagem["Subject"] = "pedido criado"
    
    mensagem.attach(MIMEText(corpo, "plain"))
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(__obter_login(), __obter_senha())
            servidor.send_message(mensagem)
            print("E_mail evnidado com sucesso ✅")
    except Exception as a: 
          print("erro ao enviar e-mail: ", a)

def enviar_email_pedido(destinatario: str, tamanho: str, sabores: list[str]):
     mensagem = f""" pedido criado com sucesso ! 
     tamanho: {tamanho}
     sabores: {",".join(sabores)} 
     """

     enviar(destinatario, mensagem)
