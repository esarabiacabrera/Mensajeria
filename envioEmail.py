import smtplib
from email.message import EmailMessage

def enviar(emailDestino,mensaje):
  emailOrigen="edinsonsarabia@uninorte.edu.co"
  password='12345679x63E'
  email=EmailMessage()
  email['From']=emailOrigen
  email['To']=emailDestino
  email['Subject']='Codigo de Activación'
  email.set_content(mensaje)

  #Send email
  smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
  smtp.starttls()
  smtp.login(emailOrigen,password)
  smtp.sendmail(emailOrigen,emailDestino, email.as_string())
  smtp.quit() 

