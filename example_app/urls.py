from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/demo', views.demo, name='demo'),
    path('/mytemplate', views.templateExample, name='mytemplate'),
    path('/temp', views.temp, name='demo2'),
    path('/imagedemo', views.imageDemo, name='imagedemo'),
    path('/ajax_demo', views.ajax_demo, name="ajax"),
    path('/baked_goods', views.baked_goods, name="baked-goods"),
    path('/date_picker', views.date_picker, name="date-picker")
]