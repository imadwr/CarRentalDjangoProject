# Generated by Django 4.2 on 2023-05-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcarsapp', '0008_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='dateReservation',
            field=models.DateField(null=True),
        ),
    ]
