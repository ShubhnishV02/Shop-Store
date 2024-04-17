from django.http import HttpResponse
from django.shortcuts import render
from store.models import *

import random


def home(request):
    productdata = Product.objects.filter(status=0)
    shuffled_products = list(productdata)
    random.shuffle(shuffled_products)                           # this is used to show the random products on the home page from all the products.


    category = Category.objects.filter(status=0)

    shuffled_categories = list(category)                         # this is used to show the random category products on the home page
    random.shuffle(shuffled_categories)

    context = {"category" : shuffled_categories[:6], "productdata" : shuffled_products[:18]}
    return render(request, "index.html" , context)


def ABOUT(request):
    return render(request, "About.html")


def CONTACT(request):
    return render(request, "Contact.html")


def PRIVACYPOLICY(request):
    return render(request, "PrivacyPolicy.html")


def TERMSandCONDITIONS(request):
    return render(request, "TermsAndConditions.html")


def FAQS(request):
    return render(request, "FAQs.html")

