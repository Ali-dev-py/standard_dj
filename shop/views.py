from django.shortcuts import render , get_object_or_404
from .models import Category , Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
            'categories':categories,
            "category":category,
            "products":products
    }
    return render(request, 'shop/list.html', context)



def product_detail(request,id,slug):
    product = get_object_or_404(Product, id=id , slug=slug)
    context = {
        'product':product
    }
    return render(request, "shop/detail.html", context)