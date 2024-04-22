from django.urls import path
from store import views
from . import views
from store.controller import authview, cart, checkout, orders

urlpatterns = [
    path('product/', views.PRODUCTS, name="product"),
    path('category_selected/', views.CATEGORY_SELECTED, name="category_selected"),
    path('product/<str:slug>', views.PRODUCTSView, name="productview"),
    path('product/<str:cate_slug>/<str:prod_slug>', views.PRODUCTDETAILS, name="product-details"),


    path('searchProduct/', views.SearchProduct, name="searchProduct"),


    path('signup/', authview.SIGNUP, name="signup"),
    path('login/', authview.LOGIN, name="loginpage"),
    path('logout/', authview.LOGOUT, name="logoutpage"),



    path('cart/', cart.CART, name="cart"),
    path('add-to-cart/', cart.ADDTOCART, name="addtocart"),
    path('update-cart/', cart.UPDATEcart, name="updatecart"),
    path('delete-cart-item/', cart.DELETEcartitem, name="deletecartitem"),



    path('checkout/', checkout.CHECKOUT, name="checkout"),
    path('place-order/', checkout.placeORDER, name="placeorder"),
    


    path('my-orders/', orders.ORDERs, name="myorders"),
    path('view-order/<str:t_no>', orders.ORDERVIEW, name="orderview"),




    # Catch-all pattern (should be placed at the end)
    path('<path>', views.catch_all_view),

    
]