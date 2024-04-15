from store.models import Cart

def get_cart(user):
    return Cart.objects.filter(user=user)