# Generated by Django 2.2.6 on 2020-05-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_orderitem_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='crust',
            field=models.CharField(default='Hand Tossed Pizza', max_length=30),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(default='Medium', max_length=30),
        ),
    ]
