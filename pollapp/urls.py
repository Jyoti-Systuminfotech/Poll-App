from django.urls import path
from pollapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getquery',views.getquery,name='getquery'),
]