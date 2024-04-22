from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

from django.db.models import Q



def catch_all_view(request, path):
    return render(request, "auth/PageNotFound.html")



def PRODUCTS(request):
    productdata = Product.objects.filter(status=0)
    out_of_stock_products = Product.objects.filter(quantity=0)
    category = Category.objects.filter(status=0)
    context = {"category" : category, "productdata" : productdata , 'out_of_stock_products':out_of_stock_products , 'title': 'Products | Shop Store'}
    return render(request, "Products.html" , context)


def CATEGORY_SELECTED(request):
    return render(request, "Category_Selection.html")



def PRODUCTSView(request, slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug=slug)
        out_of_stock_products = Product.objects.filter(category__slug=slug,quantity=0)                # this is used to show outofstocks products seperately
        category_name = Category.objects.filter(slug=slug).first()
        context = {"products" : products, "category_name":category_name, 'out_of_stock_products':out_of_stock_products , 'title': 'Products | Shop Store'}
        return render(request, "Category_Selection.html" , context)
    else:
        messages.warning(request, "No such category found")
        return redirect("product")
    



def PRODUCTDETAILS(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {"products" : products, 'title': 'Product View | Shop Store'}

        else:
            messages.error(request, "No such product found")
            return redirect("product")
    else:
        messages.error(request, "No such category found")
        return redirect("product")
    return render(request,"singleProduct.html",context)




def perform_search(query):
    if not query or query.isspace():
        return []  # Return an empty list if the query is empty or whitespace-only

    allproducts = []

    # It is used for when user search a keyword and it gives the results as finding the keyword in Place name as well as the DESCRIPTION
    # mumbai_places = Mumbai.objects.filter(Q(Place_name__icontains=query) | Q(Desc__icontains=query))
    # allplaces.extend(mumbai_places)    

    all_products_list = Product.objects.filter(Q(ProdName__icontains=query) | Q(meta_Keywords__icontains=query) )
    allproducts.extend(all_products_list)


    results = allproducts
    return results


def SearchProduct(request):
    query = request.GET.get('query')
    results = perform_search(query)
    context = {
        'query': query,
        'results': results,
    }

    return render(request, "SearchPage.html", context)