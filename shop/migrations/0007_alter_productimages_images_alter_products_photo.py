# Generated by Django 4.1.3 on 2022-11-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_devise_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
