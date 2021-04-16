from smtplib import SMTP
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from common.tools.resources import get_resource_str
from common.tools.file import read_file_content, get_filename_from_path
from services.config import SMTP_CONFIG, MAIL_CONFIG


def send_mail(subject: str, sender: str, recipients: str, html: str, attachments: list = []):
    SMTP_HOST = SMTP_CONFIG.get('SMTP_HOST')
    SMTP_PORT = SMTP_CONFIG.get('SMTP_PORT')
    SMTP_USERNAME = SMTP_CONFIG.get('SMTP_USERNAME')
    SMTP_PASSWORD = SMTP_CONFIG.get('SMTP_PASSWORD')

    message = _assemble_message(subject, sender, recipients, html, attachments=attachments)
    with SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(sender, recipients, message)


def _assemble_message(subject, sender, recipients, html, attachments: list = []):
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipients

    text_part = MIMEText(html, 'html')
    message.attach(text_part)

    for attachment in attachments:
        file_part = _process_attachment(attachment)
        message.attach(file_part)

    return message.as_string()


def _process_attachment(attachment_path):
    file_part = MIMEBase('application', 'octet-stream')
    file_bytes = read_file_content(attachment_path)
    file_part.set_payload(file_bytes)
    encoders.encode_base64(file_part)

    filename = get_filename_from_path(attachment_path)
    file_part.add_header('Content-Disposition',
                         'attachment; filename=' + filename)
    return file_part
