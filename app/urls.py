from django.urls import path
from app.views import *
app_name='statements'

urlpatterns=[
    path('condition1/',condition1,name='condition1'),
    path('condition2/',condition2,name='condition2'),
    path('condition3/',condition3,name='condition3'),
    ]