from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = "catalogue"

urlpatterns = [
    # path('', views.menu_all, name='menu_all'),
    # path('menu', views.menu, name='menu'),
    path(
        "",
        RedirectView.as_view(url="bushwick-taco-company", permanent=False),
        name="menu_all",
    ),
    path("<slug:category_slug>/<slug:slug>", views.menuitem_detail, name="detail"),
    path("<slug:store_slug>", views.store_page, name="store_page"),
    path("menu/<slug:category_slug>/", views.category_list, name="category_list"),
    # path('stores', views.store_all, name='all_stores'),
    # path('dish-<slug:slug>', views.menuitem_detail, name='menuitem_detail'),
]
