from django.conf import settings
from shop.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)        
        if not cart:
            self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart['product_id'] = {'quantity':1, 'price':product.price}
        self.save()


    def save(self):
        self.session.modified = True


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart['product_id']
            self.save()


    def get_total_price(self):
        return sum(item['price'] for item in self.cart.values())

    # def total_price(self):
    #     product_ids = self.cart.keys()
    #     products = Product.objects.filter(id__in=product_ids)

    #     total_price = 0
    #     for product in products:
    #         total_price += product.price
    #     return total_price

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()