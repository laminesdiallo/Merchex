# Generated by Django 5.1.6 on 2025-03-11 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.CharField(default='A definir ', max_length=255),
        ),
        migrations.AddField(
            model_name='band',
            name='sold',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='type',
            field=models.CharField(choices=[('CONCERT', 'Concert'), ('ALBUM', 'Album'), ('MERCH', 'Merchandise'), ('MISC', 'Miscellaneous')], default='MISC', max_length=20),
        ),
        migrations.AddField(
            model_name='band',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900)]),
        ),
    ]
