from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import *

from django.contrib.auth.models import User

import random
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def CHECKOUT(request):
    rawCart = Cart.objects.filter(user=request.user)
    for item in rawCart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    
    cartitems = Cart.objects.filter(user=request.user)
    grand_total = 0
    delivery_charge = 0
    for item in cartitems:
        item_total_price = item.product.selling_price * item.product_qty
        item.total_price = item_total_price
        grand_total += item_total_price
        if grand_total < 200 :
            delivery_charge = 60
        else:
            delivery_charge = 0


    userprofile = Profile.objects.filter(user=request.user).first()

    context = {
        'cartitems':cartitems, 
        'item_total_price':item_total_price,
        'grand_total':grand_total,
        'delivery_charge':delivery_charge,
        'userprofile': userprofile
    }
    return render(request, "UserOrder/Checkout.html", context)


@login_required(login_url='loginpage')
def placeORDER(request):
    if request.method == "POST":

        currentUser = User.objects.filter(id=request.user.id).first()

        if not currentUser.first_name:                                      #so this is used for inserting the default entry for the first time user places order
            currentUser.first_name = request.POST.get('first_name')
            currentUser.last_name = request.POST.get('last_name')
            currentUser.save()

        if not Profile.objects.filter(user=request.user):
            userProfile = Profile()
            userProfile.user = request.user
            userProfile.phone = request.POST.get('phone')
            userProfile.City = request.POST.get('city')
            userProfile.address = request.POST.get('address')
            userProfile.Country = request.POST.get('country')
            userProfile.Pincode = request.POST.get('zipcode')

            userProfile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.first_name = request.POST.get('first_name')
        neworder.last_name = request.POST.get('last_name')
        neworder.email = request.POST.get('email')
        neworder.Phone = request.POST.get('phone')
        neworder.City = request.POST.get('city')
        neworder.Address = request.POST.get('address')
        neworder.Country = request.POST.get('country')
        neworder.Pincode = request.POST.get('zipcode')

        neworder.payment_mode = request.POST.get('payment_mode')
        
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price

        trackno = 'prod'+str(random.randint(11111111,99999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'prod'+str(random.randint(11111111,99999999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product= item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )

            #to decrease the product quantity from available stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()


        # To clear user's cart
        Cart.objects.filter(user=request.user).delete()

        messages.success(request, "Your order has been placed successfully")

    return redirect('home')
