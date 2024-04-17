# Generated by Django 4.2.2 on 2024-04-16 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/product')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=250)),
                ('Phone', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=150)),
                ('Address', models.TextField()),
                ('Country', models.CharField(choices=[('India', 'India')], max_length=150)),
                ('Pincode', models.CharField(max_length=150)),
                ('total_price', models.FloatField()),
                ('payment_mode', models.CharField(max_length=200)),
                ('payment_id', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for Shipping', 'Out for Shipping'), ('Completed', 'Completed'), ('Cancel', 'Cancel')], default='Pending', max_length=150)),
                ('message', models.TextField(blank=True, null=True)),
                ('tracking_no', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('City', models.CharField(max_length=150)),
                ('Country', models.CharField(choices=[('India', 'India')], max_length=150)),
                ('Pincode', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('ProdTitle', models.CharField(max_length=100)),
                ('ProdName', models.CharField(default='', max_length=150)),
                ('product_imageMain', models.ImageField(default='', upload_to='images/product')),
                ('product_image2', models.ImageField(default='', upload_to='images/product')),
                ('product_image3', models.ImageField(default='', upload_to='images/product')),
                ('product_image4', models.ImageField(default='', upload_to='images/product')),
                ('product_image5', models.ImageField(default='', upload_to='images/product')),
                ('selling_price', models.FloatField()),
                ('original_price', models.FloatField()),
                ('Prod_Desc', models.TextField()),
                ('quantity', models.IntegerField()),
                ('off_On_Product', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('tag', models.CharField(blank=True, max_length=150, null=True)),
                ('Key_Feature', models.CharField(blank=True, max_length=1000, null=True)),
                ('Unit', models.CharField(blank=True, max_length=150, null=True)),
                ('Net_Weight', models.CharField(blank=True, max_length=100, null=True)),
                ('Shelf_Life', models.CharField(blank=True, max_length=150, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('meta_Keywords', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
