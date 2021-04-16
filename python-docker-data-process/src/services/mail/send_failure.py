from common.tools.mail import send_mail
from common.tools.datetime import get_current_datetime_str
from common.tools.resources import get_resource_str
from services.config import MAIL_CONFIG


def run():
    subject = MAIL_CONFIG.get('MAIL_SUBJECT')
    sender = MAIL_CONFIG.get('MAIL_SENDER')
    recipients = MAIL_CONFIG.get('MAIL_RECIPIENTS')
    mail_enabled = MAIL_CONFIG.get('MAIL_ENABLED')

    if mail_enabled:
        template = get_resource_str('mails/failure_mail.html')
        html = template.format(process_datetime=get_current_datetime_str())
        attachments = ['app.log']
        send_mail(subject, sender, recipients, html, attachments=attachments)
