# Generated by Django 4.2.5 on 2023-11-05 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_cartlist_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='status',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
    ]