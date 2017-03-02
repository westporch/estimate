from django.shortcuts import get_object_or_404, render
from estimate.models import Product

#def index(request):
#    product_list = Product.objects.all()
#    context = {'product_list': product_list}
#    return render(request, 'estimate/index.html', context)

def index(request):
    product_list = Product.objects.all()

    price = 1000000
    #context = {'product_list': product_list, 'test_price': price, 'get_price': Product.objects.values('unit_price')}
    context = {'product_list': product_list, 'test_price': price, 'get_price': Product.objects.values('unit_price')}
    #context = {'product_list': product_list, 'test_price': price, 'get_price': Product.objects.filter(item_name='U+XEN')}

    return render(request, 'estimate/index.html', context)
