from django.shortcuts import render
from. models import Product
from .forms import ProductForm

# Create your views here.
def index99(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ProductForm()
    

    context = {
        "products" : products,
        "form" : form
    }

    return render(request, 'index99.html', context)







