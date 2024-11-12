from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('form1/', views.form1_view, name='form1'),
    path('form2/', views.form2_view, name='form2'),
    path('form1_list/', views.form1_list, name='form1_list'),
    path('form2_list/', views.form2_list, name='form2_list'),
    path('form1/edit/<int:id>/', views.edit_form1, name='edit_form1'),
    path('form1/delete/<int:id>/', views.delete_form1, name='delete_form1'),
    path('form2/edit/<int:id>/', views.edit_form2, name='edit_form2'),
    path('form2/delete/<int:id>/', views.delete_form2, name='delete_form2'),
]