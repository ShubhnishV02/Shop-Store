"""
URL configuration for ShubhnishStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ShubhnishStore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.ABOUT, name="about"),
    path('contact/', views.CONTACT, name="contact"),
    path('privacy-policy/', views.PRIVACYPOLICY, name="privacy-policy"),
    path('terms-and-conditions/', views.TERMSandCONDITIONS, name="terms-and-conditions"),
    path('faqs/', views.FAQS, name="faqs"),


    path('singleproduct/', views.SINGLEPRODUCT, name="singleproduct"),
    path('product/', views.PRODUCTS, name="product"),



    path('login/', views.LOGIN, name="login"),
    path('signup/', views.SIGNUP, name="signup"),
]
