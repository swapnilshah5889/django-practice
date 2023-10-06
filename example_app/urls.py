from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/demo', views.demo, name='demo'),
    path('/mytemplate', views.templateExample, name='mytemplate'),
    path('/temp', views.temp, name='demo2'),
]