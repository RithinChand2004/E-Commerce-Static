from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('form1/', views.form1_view, name='form1'),
    path('form2/', views.form2_view, name='form2'),
]