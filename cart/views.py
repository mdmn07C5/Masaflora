from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from tacobar.models import MenuItem

# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    return render(request=request, template_name='tacobar/cart/summary.html', context={'cart':cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        print(request.POST)
        menuitem_id = int(request.POST.get('menuitemid'))
        menuitem_qty = int(request.POST.get('menuitemqty'))
        menuitem = get_object_or_404(MenuItem, id=menuitem_id)
        cart.add(menuitem=menuitem, menuitemqty=menuitem_qty)
        response = JsonResponse({'qty': len(cart), 'item_qty':cart.cart[str(menuitem_id)]['qty']})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        menuitem_id = int(request.POST.get('menuitemid'))
        cart.delete(menuitem_id=menuitem_id)
        response = JsonResponse({'Success': True})
        return response