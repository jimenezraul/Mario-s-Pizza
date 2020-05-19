# Generated by Django 2.2.6 on 2020-05-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20200512_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='crust_type',
            field=models.CharField(choices=[('Hand Tossed Pizza', 'Hand Tossed Pizza'), ("Thin 'N Crispy", "Thin 'N Crispy"), ('Original Pan', 'Original Pan'), ('Original Stuffed Crust', 'Original Stuffed Crust')], default='Hand Tossed Pizza', max_length=30),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=8.99, max_digits=6),
        ),
    ]
