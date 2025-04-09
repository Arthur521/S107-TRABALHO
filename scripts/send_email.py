import os
import smtplib
from email.message import EmailMessage

def enviar_email(destinatario):
    msg = EmailMessage()
    msg.set_content("Pipeline executado com sucesso!")
    msg['Subject'] = "Notificação do Pipeline"
    msg['From'] = os.environ["SMTP_USER"]
    msg['To'] = destinatario

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as smtp:
            smtp.starttls()
            smtp.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
            smtp.send_message(msg)
        print("E-mail enviado com sucesso via Outlook!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    destinatario = os.getenv("EMAIL_DESTINO")
    if not destinatario:
        raise ValueError("Variável de ambiente EMAIL_DESTINO não está definida.")
    enviar_email(destinatario)
