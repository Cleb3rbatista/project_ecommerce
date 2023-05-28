from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.home, name = 'home'),
    path('cadastro/',views.cadastro, name = 'cadastro'),
    path('login/', views.login_view, name = 'login'),
    path('login/pesquisaprodutos/', views.pesquisaprodutos, name = 'pesquisaprodutos'),
    path('logout/', views.logout_view, name='logout'),
]