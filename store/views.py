from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.


def Homepage(request):
    all_product = Product.objects.all()
    context = {"all_products": all_product}
    return render(request, "store/home.html", context)

def singleproduct(request, input_id):
    current_product = Product.objects.get(id=input_id)
    context = {"product": current_product}
    return render(request, "store/single.html", context)


def contactpage(request):
    return render(request, "store/contact.html",)

