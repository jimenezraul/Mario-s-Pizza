# Generated by Django 2.2.6 on 2020-05-12 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0003_auto_20200512_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
