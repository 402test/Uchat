from django.urls import path
from users.views import LoginView,RegisterView
app_name='users'
urlpatterns=[
    path('login/',LoginView,name='login'),
path('register/',RegisterView,name='register')
]