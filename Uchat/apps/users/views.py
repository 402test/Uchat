from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.

# class LoginView(TemplateView):
#     template_name = 'user/login.html'
from users.form import RegisterForm

import random

def Register_Code_View(request,uuid):
    if request.method == 'GET':
        return render(request, 'templates/user/register_code.html', {'uuid': uuid})


def LoginView(request):
    if request.method=='GET':
        register_form = RegisterForm()
        return render(request,'user/login.html',{'register_form':register_form})
    if request.method == 'POST':
        pass

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

                pass
            else:
                # 短信发送失败
                message = '短信发送失败'
                messages.error(request, message)
                return render(request, 'user/register.html', {'register_form': form_obj})
            return redirect(reverse('users:login'))
        else:
            return  render(request,'user/register.html',{'register_form':form_obj})



