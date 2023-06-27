from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('landing/', views.landing_view, name='landing'),
]
