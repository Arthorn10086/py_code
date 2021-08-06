import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = 'smtp.qq.com'
mail_port = 465


def qq_normal(mail_user, mail_pw, receivers, content, content_type, fromer=None, toer=None, subject=''):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式|html html格式，第三个 utf-8 设置编码
    message = MIMEText(content, content_type, 'utf-8')
    if not fromer:
        fromer = mail_user
    if not toer:
        toer = receivers[0]
    message['From'] = Header(fromer, 'utf-8')  # 发送者
    message['To'] = Header(toer, 'utf-8')  # 接收者
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.connect(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pw)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as err:
        print("Error: 无法发送邮件", err)


def qq_complex(mail_user, mail_pw, receivers, content, content_type, annex, fromer=None, toer=None, subject=''):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    if not fromer:
        fromer = mail_user
    if not toer:
        toer = receivers[0]
    message = MIMEMultipart()
    message['From'] = Header(fromer, 'utf-8')  # 发送者
    message['To'] = Header(toer, 'utf-8')  # 接收者
    message['Subject'] = Header(subject, 'utf-8')
    # 正文
    message.attach(MIMEText(content, content_type, 'utf-8'))
    # 附件
    for fn, fpath in annex:
        att1 = MIMEText(open(fpath, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = f'attachment; filename="{fn}"'
        message.attach(att1)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.connect(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pw)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as err:
        print("Error: 无法发送邮件", err)

