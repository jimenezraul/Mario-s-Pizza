# Generated by Django 2.2.6 on 2020-05-18 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0010_auto_20200517_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='sandwich',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza.Sandwiches'),
        ),
    ]