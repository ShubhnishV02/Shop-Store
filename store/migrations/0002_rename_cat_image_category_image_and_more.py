# Generated by Django 4.2.2 on 2024-04-09 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Cat_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Cat_name',
            new_name='name',
        ),
    ]
