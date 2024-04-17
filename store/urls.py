from django.urls import path
from store import views
from store.controller import authview, cart, checkout

urlpatterns = [
    path('product/', views.PRODUCTS, name="product"),
    path('category_selected/', views.CATEGORY_SELECTED, name="category_selected"),
    path('product/<str:slug>', views.PRODUCTSView, name="productview"),
    path('product/<str:cate_slug>/<str:prod_slug>', views.PRODUCTDETAILS, name="product-details"),


    path('signup/', authview.SIGNUP, name="signup"),
    path('login/', authview.LOGIN, name="loginpage"),
    path('logout/', authview.LOGOUT, name="logoutpage"),



    path('cart/', cart.CART, name="cart"),
    path('add-to-cart/', cart.ADDTOCART, name="addtocart"),
    path('update-cart/', cart.UPDATEcart, name="updatecart"),
    path('delete-cart-item/', cart.DELETEcartitem, name="deletecartitem"),



    path('checkout/', checkout.CHECKOUT, name="checkout"),
    path('place-order/', checkout.placeORDER, name="placeorder"),
    
]