from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *



def PRODUCTS(request):
    productdata = Product.objects.filter(status=0)
    category = Category.objects.filter(status=0)
    context = {"category" : category, "productdata" : productdata}
    return render(request, "Products.html" , context)

def CATEGORY_SELECTED(request):
    return render(request, "Category_Selection.html")


def PRODUCTSView(request, slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {"products" : products, "category_name":category_name}
        return render(request, "Category_Selection.html" , context)
    else:
        messages.warning(request, "No such category found")
        return redirect("product")
    

def PRODUCTDETAILS(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {"products" : products}

        else:
            messages.error(request, "No such product found")
            return redirect("product")
    else:
        messages.error(request, "No such category found")
        return redirect("product")
    return render(request,"singleProduct.html",context)