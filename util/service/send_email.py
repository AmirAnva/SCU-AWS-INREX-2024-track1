import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

def send_email(recipient_email, subject, body):
    load_dotenv()
    sender_email = os.getenv("sender_email")
    sender_password = os.getenv("sender_password")
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail SMTP server and start TLS (Transport Layer Security)
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the server
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)

        # Disconnect from the server
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")
