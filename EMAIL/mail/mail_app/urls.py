from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('set', views.setsession, name='set'),
    path('get', views.getsession, name='get'),
    path('reg', views.reg, name='reg'),
    
  
]