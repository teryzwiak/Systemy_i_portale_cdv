from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('mainpage', views.myapp, name='myapp'),
    path('test.html', views.test, name='test'),
    path('loginpage', views.loginpage, name='loginpage')
]