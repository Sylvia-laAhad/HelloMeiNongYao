from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    ##path('getCoockie/', views.checkVisitCookie, name='getCookie')
]