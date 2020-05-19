# Generated by Django 2.2.6 on 2020-05-18 02:00

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0007_auto_20200517_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sandwiches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('combo', models.CharField(choices=[('Meal', 'Meal'), ('Sandwich', 'Sandwich')], default='Meal', max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Medium', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=8.99, max_digits=6)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]