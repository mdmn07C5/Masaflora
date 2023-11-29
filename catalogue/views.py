from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem, Store, Option


def store_all(request):
    stores = Store.objects.all()
    return render(
        request=request,
        template_name="catalogue/stores/stores.html",
        context={"stores": stores},
    )


def store_page(request, store_slug):
    store = get_object_or_404(Store, slug=store_slug)
    menu = store.get_menu()

    return render(
        request=request,
        template_name="catalogue/stores/store_page.html",
        context={"store": store, "menu": menu},
    )


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    menuitems = MenuItem.objects.filter(category=category)
    return render(
        request=request,
        template_name="catalogue/menu/category.html",
        context={"category": category, "menuitems": menuitems},
    )


def menu_all(request):
    menuitems = MenuItem.menuitems.all()
    return render(
        request=request,
        template_name="catalogue/home.html",
        context={"menuitems": menuitems},
    )


def menuitem_detail(request, slug):
    menuitem = get_object_or_404(MenuItem, slug=slug, is_available=True)
    return render(
        request=request,
        template_name="catalogue/menu/detail.html",
        context={"menuitem": menuitem},
    )


def menu(request):
    menuitems = MenuItem.menuitems.all()
    return render(
        request=request,
        template_name="catalogue/menu/menu.html",
        context={"menuitems": menuitems},
    )
