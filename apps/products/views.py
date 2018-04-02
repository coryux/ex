from django.shortcuts import render

def products(request):
    return render(request,'products/products.html')

def product(request, number):
    return render(request,'products/products.html', {'number':number})
