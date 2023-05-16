import os
import smtplib
from email.message import EmailMessage

user_gmail = os.getenv('USER_GMAIL')
password_gmail = os.getenv('PASSWORD_GMAIL')

def send_notifying_mail(mail_user: str = "", mail_password: str = "") -> None:
    # aqui va tu codigo
    msg = EmailMessage()
    # Contenido
    msg['From']="anaasendon@gmail.com"
    msg['To']="anaasendon@gmail.com"
    msg['Subject']= "Beep beep u sad fuck!"
    cuerpo_del_mail = 'https://www.youtube.com/watch?v=bXocfwP-hMc =D'
    msg.set_content(cuerpo_del_mail)

    # No se queden en los detalles aquí, pero pueden leer más sobre el protocolo SMTP acá: https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Usuario y contraseña
    usuario = 'mi_usuario'

    server.login(user_gmail, password_gmail)

    # enviar
    server.send_message(msg)
    server.quit();


  if __name__ == "__main__":
      enviar_mail(user_gmail, password_gmail) # modificar segun se llame tu funcion
