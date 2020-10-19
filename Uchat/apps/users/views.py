from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from users.models import User
# Create your views here.

# class LoginView(TemplateView):
#     template_name = 'user/login.html'
from users.form import RegisterForm, LoginForm
from users.models import PhoneCode

import random

def Register_Code_View(request,uuid):
    if request.method == 'GET':
        return render(request, 'templates/user/register_code.html', {'uuid': uuid})
    if request.method=='POST':
        uuid = request.POST['uuid']
        code = request.POST.get('pcode')
        if not code:
            messages.error(request, '验证码不能为空')
            return redirect(reverse('users:register_code', kwargs={'uuid': uuid}))

        user = get_object_or_404(User,uuid=uuid)
        if user.pcode.code ==code:
            user.is_active =True
            return redirect(reverse('users:login'))
        else:
            messages.error(request, '验证码错误')
            return redirect(reverse('users:register_code' ,kwargs={'uuid':uuid}))


def LoginView(request):
    if request.method=='GET':
        register_form = RegisterForm()
        return render(request,'user/login.html',{'register_form':register_form})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
        if user and user.is_active:
            login(request, user)
            messages.success(request, "自动跳转到主页", extra_tags="登录成功！")
            return HttpResponseRedirect(reverse("sspanel:userinfo"))




def RegisterView(request):
    if request.method=='GET':
        register_form = RegisterForm()
        return render(request,'user/register.html',{'register_form':register_form})
    if request.method == 'POST':
        form_obj = RegisterForm(request.POST)
        if form_obj.is_valid():
            #  如果通过基本验证  则发送短信
            code = random.randint(1000, 10000)
            if code:
                # 短信发送正常
                form_obj.cleaned_data['username'] =  form_obj.cleaned_data['phone']
                user = User.add_new_user(form_obj.cleaned_data)
                PhoneCode.objects.create(code=code,user=user)
                message = '短信发送成功'
                messages.success(request,message)
                return redirect(reverse('users:register_code',kwargs = {'uuid':user.uuid}))
            else:
                # 短信发送失败
                message = '短信发送失败'
                messages.error(request, message)
                return render(request, 'user/register.html', {'register_form': form_obj})
            return redirect(reverse('users:login'))
        else:
            return  render(request,'user/register.html',{'register_form':form_obj})



