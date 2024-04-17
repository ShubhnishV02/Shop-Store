from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import *

from django.contrib.auth.decorators import login_required



def ADDTOCART(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                     return JsonResponse({'status': "Product already in Cart"})  
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty :
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product Added Successfully"})  
                    else:
                        return JsonResponse({'status': "Only"+ str(product_check.quantity) +" quantity available" })

            else:
                return JsonResponse({'status': "No such product found"})

        else:
            return JsonResponse({'status': "Login to Continue"})

    return redirect("home")


def UPDATEcart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()

            return JsonResponse({'status': 'Updated Successfully'})
    return redirect('home')


def DELETEcartitem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()

            return JsonResponse({'status': 'Deleted Successfully'})
    return redirect('home')


@login_required(login_url='loginpage')
def CART(request):    
    cartitems = Cart.objects.filter(user=request.user)
    grand_total = 0
    delivery_charge = 0
    shop_for_more = 0
    for item in cartitems:
        total_price = item.product.selling_price * item.product_qty
        item.total_price = total_price
        grand_total += total_price
        if grand_total < 200 :
            delivery_charge = 60
            shop_for_more = 200 - grand_total
        else:
            delivery_charge = 0
            shop_for_more = 0


    context = {
        'cartitems':cartitems, 
        'grand_total':grand_total,
        'delivery_charge':delivery_charge,
        'shop_for_more':shop_for_more,
    }
    return render(request, "auth/Cart.html", context)