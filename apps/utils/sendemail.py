from random import Random

from django.core.mail import send_mail

from users.models import EmailVerificationCode
from muxuewang.settings import EMAIL_FROM

def generate_random_str(length):
    """返回一个长度为length的随机字符串"""

    random_string = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    chars_length = len(chars) - 1
    random = Random()
    for i in range(length):
        random_string += chars[random.randint(0, chars_length)]
    return random_string

def send_verification_email(email, send_type='register'):
    code = generate_random_str(16)
    emailvc = EmailVerificationCode()
    emailvc.code = code
    emailvc.email = email
    emailvc.sent_type = send_type
    emailvc.save()

    if send_type == 'register':
        email_title = '慕学网用户注册激活'
        email_body = '请点击以下链接激活用户：http://127.0.0.1:8000/active/%s/'%code

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print('发送成功')