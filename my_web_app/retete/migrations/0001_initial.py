# Generated by Django 4.0.1 on 2022-02-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reteta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_reteta', models.CharField(max_length=100)),
                ('tip_produs', models.CharField(max_length=100)),
                ('cantitate', models.IntegerField()),
                ('um', models.CharField(max_length=10)),
            ],
        ),
    ]
