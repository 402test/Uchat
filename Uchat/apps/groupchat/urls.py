from django.urls import path
from groupchat.views import IndexView,Tourist_Register_View
app_name='groupchat'
urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('tourist_register',Tourist_Register_View,name='tourist_register')
]