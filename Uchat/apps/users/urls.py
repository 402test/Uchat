from django.urls import path
from users.views import LoginView,RegisterView,Register_Code_View
app_name='users'
urlpatterns=[
    path('login/',LoginView,name='login'),
path('register/',RegisterView,name='register'),
    path('register_code/<uuid>',Register_Code_View,name='register_code')
]