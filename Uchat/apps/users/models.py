
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class User(AbstractUser):
    uuid =  models.UUIDField(default=uuid.uuid4)
    nickname = models.CharField(null=True, blank=True, max_length=255, verbose_name='昵称')
    picture = models.ImageField(upload_to='media/profile_pics/', null=True, blank=True, verbose_name='头像')
    phone = models.CharField(max_length=12,unique=True,verbose_name='手机号码')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')



class VerifyCode(models.Model):
    '''邮箱验证码'''
    code = models.CharField(verbose_name='验证码', max_length=10)
    email = models.EmailField(verbose_name='邮箱', default='')
    send_choices = (
        ('register', '注册'),
        ('forget', '找回密码'),
        ('update_email', '修改邮箱')
    )
    send_type = models.CharField(verbose_name='验证码类型', max_length=30, choices=send_choices, default='register')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

