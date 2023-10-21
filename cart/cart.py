

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
