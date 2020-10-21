from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
import random
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_http_methods
import json

class IndexView(View):
    def get(self,request):
        #  判断有没有登录状态   判断有没有游客登录cookie    有的话  直接跳转到 主页  ， 没有的话  就进入游客登录页面
        if not request.user.is_authenticated:
            #  没有登录
            cookie_info = request.COOKIES.get('nickname')
            if not cookie_info:
                return render(request,'templates/groupchat/register.html')
        return render(request, 'templates/groupchat/index.html',{'nickname':json.loads(cookie_info)})

@require_http_methods(["POST"])
def Tourist_Register_View(request):
    if request.method =='POST':
        L = [
            '仙中仙儿',
            '人狠词稳',
            '大佬裙下',
            '虚假暧昧',
            '峥骨野风',
            '生死契阔',
            '温柔野鬼',
            '掌中江山',
            '神的宿敌',
            '满身戾气',
            '情深依旧',
            '网混男孩',
            '佳雨时节',
            '半纸风雪',
            '西风渡口',
            '甜蜜且乖',
            '同心偕老',
            '风起水浪',
            '折尽梅花',
            '温柔劣人',
            '笑对时光',
            '竹隐寒烟',
            '南風未起',
            '白丝妖娆',
            '指尖冰凉',
            '青莲白雾',
            '深海未及',
            '乱世惊梦',
            '乱世浮华',
            '白栀长衫',
            '千城墨白',
            '临窗赏雨',
            '深海不蓝',
            '梦与时光',
            '埋葬回憶',
            '樱兰静雪',
            '王者梦晓',
            '北岛樱花',
            '红颜流逝',
            '记忆之城',

        ]
        nickname = request.POST.get('nickname')
        if not nickname or len(nickname)>10:
            nickname = random.choice(L)

        rep = redirect(reverse('groupchat:index'))
        rep.set_cookie('nickname',json.dumps(nickname),max_age=60*60*12)
        return rep






