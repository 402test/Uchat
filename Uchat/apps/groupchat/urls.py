from django.urls import path
from groupchat.views import IndexView
app_name='groupchat'
urlpatterns=[
    path('',IndexView.as_view(),name='index'),
]