# Generated by Django 4.1.3 on 2022-11-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_products_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, upload_to='single/image'),
        ),
    ]
