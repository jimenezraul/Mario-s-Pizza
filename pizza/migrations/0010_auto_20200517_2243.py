# Generated by Django 2.2.6 on 2020-05-18 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0009_ordersandwiches'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item',
            new_name='pizza',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='combo',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='sandwich',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.Sandwiches'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='crust',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.DeleteModel(
            name='OrderSandwiches',
        ),
    ]
