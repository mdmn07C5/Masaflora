from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .cart import Cart
from catalogue.models import MenuItem, Option

# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    return render(
        request=request, template_name="cart/summary.html", context={"cart": cart}
    )


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        menuitem_id = int(request.POST.get("menuitemid"))
        menuitem_qty = int(request.POST.get("menuitemqty"))
        options = request.POST.get("options")
        menuitem = get_object_or_404(MenuItem, id=menuitem_id)
        sub_total = cart.add(menuitem=menuitem, options=options)
        response = JsonResponse(
            {
                "qty": len(cart),
                "sub_total": sub_total,
                "total": cart.get_total(),
            }
        )
        return response


def option_info(request):
    if request.GET.get("action") == "get":
        option_id = int(request.GET.get("optionid"))
        option = get_object_or_404(Option, id=option_id)
        response = JsonResponse(
            {
                "id": option.id,
                "name": option.name,
                "price": option.price,
            }
        )
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        menuitem_id = int(request.POST.get("menuitemid"))
        cart.delete(menuitem_id=menuitem_id)
        response = JsonResponse({"qty": len(cart), "total": cart.get_total()})
        return response
