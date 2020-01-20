from django.urls import path
from . import views

urlpatterns=[
    #path('',views.index,name='index'),
    path('',views.dynamic_form,name='dynamic_form'),
    path('second/',views.second,name='second'),
]