# Generated by Django 4.2 on 2023-05-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcarsapp', '0011_reservation_paye'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]
