import os
import smtplib
from email.message import EmailMessage

destino = os.getenv("EMAIL_DESTINO")

if not destino:
    raise ValueError("EMAIL_DESTINO não está configurado.")

msg = EmailMessage()
msg.set_content("Pipeline executado com sucesso!")
msg['Subject'] = 'Notificação do Pipeline'
msg['From'] = "seu_email@gmail.com"  # pode estar fixo
msg['To'] = destino

# Exemplo com Gmail (você pode usar outro servidor SMTP)
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("seu_email@gmail.com", "SENHA_AQUI")
        smtp.send_message(msg)
    print("E-mail enviado com sucesso.")
except Exception as e:
    print(f"Erro ao enviar o e-mail: {e}")
