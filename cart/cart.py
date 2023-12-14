from catalogue.models import MenuItem, Option
from decimal import Decimal
import pprint
import json
import hashlib


class Cart:
    """Session wrapper for Cart model"""

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_cart")
        if "session_cart" not in request.session:
            cart = self.session["session_cart"] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, menuitem, options):
        """Add/update user's cart session data

        Args:
            menuitem (MenuItem): the item to add  into the cart
        """
        items = self.cart.get("items", [])

        try:
            opts = {}
            for op in json.loads(options):
                o = Option.objects.get(id=op)
                opts[o.id] = {
                    "name": o.name,
                    "price": str(o.price),
                }
        except:
            opts = {}

        item = {
            "id": str(menuitem.id),
            "name": str(menuitem.name),
            "price": str(menuitem.price),
            "options": opts,
        }
        items.append(item)
        self.cart["items"] = items
        self.save()

        return self.get_sub_total(-1)

    def delete(self, index):
        """Delete menuitem from cart

        Args:
            index (int): index of the item to delete
        """
        # if index in self.cart.items:
        #     del self.cart.items[index]
        #     self.save()
        del self.cart["items"][index]
        self.save()

    def get_sub_total(self, item_index):
        item = self.cart["items"][item_index]
        sub_total = Decimal(item["price"])
        for op in item["options"].values():
            sub_total += Decimal(op["price"])
        return sub_total

    def get_total(self):
        total = Decimal(0)
        for i, item in enumerate(self.cart["items"]):
            total += +Decimal(self.get_sub_total(i))
        return total

    def __len__(self):
        # pprint(self.cart.items(), )
        # pprint.pp(self.cart.items())
        return len(self.cart.get("items", []))

    def __iter__(self):
        """Collect menuitem id from session data to query db and return menuitems"""
        menuitem_ids = [item["id"] for item in self.cart["items"]]
        menuitems = MenuItem.objects.filter(id__in=menuitem_ids)

        cart = self.cart.copy()

        for i, item in enumerate(cart["items"]):
            item["menuitem"] = menuitems.get(id=item["id"])
            item["total_price"] = self.get_sub_total(i)
            yield i, item
