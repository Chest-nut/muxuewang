from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10,
                              choices=(('male', '男'), ('female', '女')),
                              default='female')
    address = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True)
    avatar = models.ImageField(max_length=100,
                               upload_to='avatar/%Y/%m',
                               default='avatar/default.png',
                               blank=True)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class EmailVerificationCode(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50)
    sent_type = models.CharField(choices=(('register', '注册'), ('forget', '找回密码')),
                                 max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(max_length=100,
                              upload_to='banner/%Y/%m',
                              verbose_name='轮播图')
    url = models.URLField(max_length=200, verbose_name='跳转地址')
    order = models.SmallIntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name