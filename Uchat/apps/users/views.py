from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.

# class LoginView(TemplateView):
#     template_name = 'user/login.html'
from users.form import RegisterForm


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
            #register_form = RegisterForm()  #  修改为登录得 form
            print('登录成功')
            return redirect(reverse('users:login'))
        else:
            return  render(request,'user/register.html',{'register_form':form_obj})
