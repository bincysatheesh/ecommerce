# Generated by Django 4.2.5 on 2023-11-05 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_cartitem_tot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='tot',
            new_name='t',
        ),
    ]