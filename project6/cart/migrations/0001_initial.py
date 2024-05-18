# Generated by Django 5.0.4 on 2024-04-29 09:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


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
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Catagory',
                'verbose_name_plural': 'Catagories',
            },
        ),
        migrations.CreateModel(
            name='ColourVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SizeVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=290)),
                ('zip_code', models.CharField(max_length=290)),
                ('default', models.BooleanField(default=False)),
                ('address_line_1', models.CharField(max_length=290)),
                ('address_line_2', models.CharField(max_length=290)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('ordered_date', models.DateField(blank=True, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='cart.address')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='cart.address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('raw_response', models.TextField()),
                ('successfull', models.BooleanField(default=False)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('payment_methode', models.CharField(choices=[('PayPal', 'PayPal')], max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='cart.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('stock', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=190)),
                ('active', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='product_images')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('available_colours', models.ManyToManyField(to='cart.colourvariation')),
                ('primary_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_products', to='cart.category')),
                ('secondary_categories', models.ManyToManyField(blank=True, to='cart.category')),
                ('available_sizes', models.ManyToManyField(to='cart.sizevariation')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.colourvariation')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.sizevariation')),
            ],
        ),
        migrations.CreateModel(
            name='StripePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('successfull', models.BooleanField(default=False)),
                ('payment_intent_id', models.CharField(max_length=100)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stripe_payments', to='cart.order')),
            ],
        ),
    ]