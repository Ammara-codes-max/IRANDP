import smtplib
from email.mime.text import MIMEText

EMAIL_FROM = "ummeammara016@gmail.com"
EMAIL_PASS = "yvqiedjropdglwch"   # <-- App Password yahan paste karo
EMAIL_TO   = "uw-23-cy-bs-034@student.uow.edu.pk"

def send_alert(subject, body):
    msg = MIMEText(body)
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASS)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print("📧 Email Alert Sent")
    except Exception as e:
        print("❌ Email Failed:", e)
