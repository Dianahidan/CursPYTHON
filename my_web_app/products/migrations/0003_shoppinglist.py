# Generated by Django 4.0.1 on 2022-02-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_um'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_produs', models.CharField(max_length=100)),
                ('cantitate', models.IntegerField()),
                ('um', models.CharField(max_length=10)),
            ],
        ),
    ]
