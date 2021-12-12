from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter , name="newsletter"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('hashrate/', views.hashrate, name="hashrate"),  
    path('privacy-policy/', views.privacy, name="privacy"),  
    
]