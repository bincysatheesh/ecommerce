# Generated by Django 4.2.5 on 2023-11-05 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_alter_cartlist_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartlist',
            name='status',
        ),
    ]
