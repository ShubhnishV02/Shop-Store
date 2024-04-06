from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")

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


def SINGLEPRODUCT(request):
    return render(request, "SingleProduct.html")

def PRODUCTS(request):
    return render(request, "Products.html")



def LOGIN(request):
    return render(request, "Login.html")

def SIGNUP(request):
    return render(request, "Signup.html")