# Generated by Django 4.2.2 on 2024-04-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='festival',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
