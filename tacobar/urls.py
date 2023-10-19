from django.urls import path
from . import views

app_name = 'tacobar'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu-detail/<slug:slug>/', views.menuitem_detail, name='menuitem_detail'),
    path('<slug:category_slug>/', views.category_list, name='category_list'),
]