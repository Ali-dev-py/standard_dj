from django.http import request
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .forms import CartAddFrom
from .cart import Cart

# from django.contrib.auth.decorators import login_required

#@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = CartAddFrom(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart.add(product)
    return redirect('cart:detail')

#@login_required
@require_POST
def cart_remove(self, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove(product)
    return redirect('cart:detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})