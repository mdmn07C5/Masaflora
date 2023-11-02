from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.menu_all, name='menu_all'),
    path('stores', views.store_all, name='all_stores'),
    path('<slug:store_slug>', views.store_page, name='store_page'),
    path('<slug:slug>', views.menuitem_detail, name='menuitem_detail'),
    path('menu/<slug:category_slug>/', views.category_list, name='category_list'),
]
