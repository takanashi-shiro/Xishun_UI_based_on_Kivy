import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import Send_Mail_config as config


def Send_Msg(to: list, title, conntent):
    try:
        msg = MIMEMultipart()
        msg_from = config['From']
        msg_pwd = config['pwd']
        msg.attach(MIMEText(conntent, 'plain', 'utf-8'))
        msg['Subject'] = title
        msg['From'] = msg_from
        s = smtplib.SMTP_SSL(config['STMP_SSL'], 465)
        s.login(msg_from, msg_pwd)
        s.sendmail(msg_from, to, msg.as_string())
        return
    except Exception as e:
        return
