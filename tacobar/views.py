from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    menuitems = MenuItem.menuitems.all()
    return render(
        request=request,
        template_name='tacobar/menu/category.html',
        context={'category':category, 'menuitems': menuitems}
    )

def menu(request):
    menuitems = MenuItem.menuitems.all()
    return render(
        request=request,
        template_name='tacobar/home.html',
        context={'menuitems':menuitems}
    )

def menuitem_detail(request, slug):
    menuitem = get_object_or_404(MenuItem, slug=slug, is_available=True)
    return render(
        request=request,
        template_name='tacobar/menu/detail.html',
        context={'menuitem':menuitem}
    )

