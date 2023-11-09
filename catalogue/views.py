from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    menuitems = MenuItem.objects.filter(category=category)
    return render(
        request=request,
        template_name='catalogue/menu/category.html',
        context={'category': category, 'menuitems': menuitems}
    )


def menu_all(request):
    menuitems = MenuItem.menuitems.all()
    return render(
        request=request,
        template_name='catalogue/home.html',
        context={'menuitems': menuitems}
    )


def menuitem_detail(request, slug):
    menuitem = get_object_or_404(MenuItem, slug=slug, is_available=True)
    return render(
        request=request,
        template_name='catalogue/menu/detail.html',
        context={'menuitem': menuitem}
    )