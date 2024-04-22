from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import *


def ORDERs(request):
    orders = Order.objects.filter(user=request.user)
    context = { 'orders': orders, 'title': 'My Orders | Shop Store' }
    return render(request, "UserOrder/Orders.html", context)


def ORDERVIEW(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderItems = OrderItem.objects.filter(order=order)

    context = { 'order':order, 'orderItems':orderItems, 'title': 'Order View | Shop Store' }
    return render(request, 'UserOrder/OrderView.html', context)
