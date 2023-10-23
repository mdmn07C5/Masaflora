from tacobar.models import MenuItem
from decimal import Decimal

class Cart():

    def __init__(self, request):
        self.session = request.session
        # self.cart = self.session.get('session_cart', {'Peepee':'PooPoo'})
        cart = self.session.get('session_cart')
        if 'session_cart' not in request.session:
            cart = self.session['session_cart'] = {}
        self.cart = cart

    def add(self, menuitem, menuitemqty):
        """Add/update user's cart session data

        Args:
            menuitem (MenuItem): the item to add  into the cart
        """
        menuitem_id = str(menuitem.id)
        self.cart[menuitem_id] = self.cart.get(
            menuitem_id, {'price': str(menuitem.price,)})
        
        qty = self.cart[menuitem_id].get('qty', 0)
        self.cart[menuitem_id]['qty'] = int(menuitemqty) + int(qty)

        self.session.modified = True

    def __len__(self): 
        return sum(item['qty'] for item in self.cart.values())
    
    def __iter__(self):
        """Collect menuitem id from session data to query db and return menuitems
        """
        menuitem_ids = self.cart.keys()
        menuitems = MenuItem.objects.filter(id__in=menuitem_ids)
        
        cart = self.cart.copy()
        for menuitem in menuitems:
            cart[str(menuitem.id)]['menuitem'] = menuitem

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
        