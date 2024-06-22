# Generated by Django 5.0.5 on 2024-05-28 23:17

import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_hotel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='available',
            field=models.PositiveIntegerField(default=20, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
        migrations.AlterField(
            model_name='trip',
            name='duration',
            field=models.PositiveSmallIntegerField(choices=[(7, 7), (14, 14), (28, 28)], default=7),
        ),
        migrations.AlterField(
            model_name='trip',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='trips', to=settings.AUTH_USER_MODEL),
        ),
    ]