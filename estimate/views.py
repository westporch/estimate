from django.shortcuts import get_object_or_404, render
from estimate.models import Product

def index(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'estimate/index.html', context)
