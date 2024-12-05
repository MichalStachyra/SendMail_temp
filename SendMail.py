import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
smtp_server = "smtp.example.com"  # Replace with your SMTP server
smtp_port = 587  # Typically 587 for TLS or 465 for SSL
username = "your_email@example.com"
password = "your_password"

# Email content
from_email = "your_email@example.com"
to_email = "recipient@example.com"
subject = "Test Email"
body = "This is a test email sent from Python."

# Create the email message
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start TLS encryption
    server.login(username, password)
    server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
