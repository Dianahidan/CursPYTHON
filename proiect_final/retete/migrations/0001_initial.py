# Generated by Django 4.0.1 on 2022-03-01 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_remove_products_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reteta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_reteta', models.CharField(max_length=100)),
                ('tip_produs', models.CharField(max_length=100)),
                ('um', models.CharField(max_length=10)),
                ('cantitate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
