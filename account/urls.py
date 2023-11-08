from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('login/', views.account_login, name='login'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    # dashboards shit
    path('dashboard/', views.dashboard, name='dashboard'),
]