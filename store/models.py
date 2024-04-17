from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to="images/product", null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    ProdTitle = models.CharField(max_length=100)
    ProdName = models.CharField(max_length=150, default='')

    product_imageMain = models.ImageField(upload_to="images/product", default='')
    product_image2 = models.ImageField(upload_to="images/product", default='')
    product_image3 = models.ImageField(upload_to="images/product", default='')
    product_image4 = models.ImageField(upload_to="images/product", default='')
    product_image5 = models.ImageField(upload_to="images/product", default='')

    selling_price = models.FloatField()
    original_price = models.FloatField()
    festival = models.CharField(max_length=200,null=True, blank=True)

    Prod_Desc = models.TextField()
    quantity = models.IntegerField(null=False, blank=False)
    off_On_Product = models.CharField(max_length=100, null=True, blank=True)

    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150, null=True, blank=True)
    
    Key_Feature = models.CharField(max_length=1000, blank=True, null=True)
    Unit = models.CharField(max_length=150, blank=True, null=True)
    Net_Weight = models.CharField(max_length=100, blank=True, null=True)
    Shelf_Life = models.CharField(max_length=150, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    meta_Keywords = models.CharField(max_length=150, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ProdTitle
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

Country_Choices = (
    ('India', 'India'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    Phone = models.CharField(max_length=150, null=False, blank=False)
    City = models.CharField(max_length=150, null=False, blank=False)
    Address = models.TextField(null=False, blank=False)
    Country = models.CharField(max_length=150, choices=Country_Choices, null=False, blank=False)
    Pincode = models.CharField(max_length=150, null=False, blank=False)

    total_price = models.FloatField(null=False, blank=False)
    payment_mode = models.CharField(max_length=200, null=False, blank=False)
    payment_id = models.CharField(max_length=250, null=True, blank=True)

    orderStatus = (
        ('Pending','Pending'),
        ('Out for Shipping','Out for Shipping'),
        ('Completed','Completed'),
        ('Cancel','Cancel')
    )
    status = models.CharField(max_length=150, choices=orderStatus, default='Pending')
    message = models.TextField(null=True, blank=True)
    tracking_no = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {} - {} ,{}'.format(self.order.id, self.order.tracking_no, self.order.first_name, self.order.Phone)
    




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False, blank=False)
    City = models.CharField(max_length=150, null=False, blank=False)
    Country = models.CharField(max_length=150, choices=Country_Choices, null=False, blank=False)
    Pincode = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

