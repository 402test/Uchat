from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self,request):
        #  判断有没有登录状态   判断有没有游客登录cookie    有的话  直接跳转到 主页  ， 没有的话  就进入游客登录页面
        if not request.user.is_authenticated:
            #  没有登录
            cookie_info = request.COOKIES.get('user')
            if not cookie_info:
                return render(request,'templates/groupchat/register.html')
        return render(request, 'templates/groupchat/index.html')







