# Generated by Django 3.1.5 on 2022-01-12 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220112_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='price',
            new_name='rentalPrice',
        ),
    ]
