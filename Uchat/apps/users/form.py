from django import forms
from users.models import User
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
import re
class RegisterForm(forms.ModelForm):
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
    password_t = forms.CharField(
        min_length=6,
        error_messages={
            "required": "不能为空",
            "invalid": "两次密码不一致",
            "min_length": "密码最少六位"
        }
    )
    class Meta:
        model = User
        fields = ["phone", "password"]

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise ValidationError('手机号有问题')
        if User.objects.filter(phone=value).first():
            raise ValidationError('该手机号码已经被注册了')  # 有问题的  如若第一次发验证码 注册失败  第二次 就注册不了了
        return value

    def clean_password_t(self):
        pwd = self.cleaned_data.get('password')
        pwd_t = self.cleaned_data.get('password_t')
        if pwd == pwd_t:
            return pwd_t
        raise ValidationError('密码不一致')

