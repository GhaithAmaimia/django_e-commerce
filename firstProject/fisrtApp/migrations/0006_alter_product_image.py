# Generated by Django 4.2.3 on 2023-09-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisrtApp', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no-image.png', upload_to='products/'),
        ),
    ]