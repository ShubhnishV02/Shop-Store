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

    context = {"category" : shuffled_categories[:6], "productdata" : shuffled_products[:19] , 'title': 'Homepage | Shop Store'}
    return render(request, "index.html" , context)


def ABOUT(request):
    data = {'title': 'About Us | Shop Store'}
    return render(request, "About.html", data)


def CONTACT(request):
    data = {'title': 'Contact Us | Shop Store'}
    return render(request, "Contact.html", data)


def PRIVACYPOLICY(request):
    data = {'title': 'Privacy Policy | Shop Store'}
    return render(request, "PrivacyPolicy.html", data)


def TERMSandCONDITIONS(request):
    data = {'title': 't&c | Shop Store'}
    return render(request, "TermsAndConditions.html", data)


def FAQS(request):
    data = {'title': 'FAQs | Shop Store'}
    return render(request, "FAQs.html", data)

