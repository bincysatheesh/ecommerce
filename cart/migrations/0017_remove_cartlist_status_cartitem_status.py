# Generated by Django 4.2.5 on 2023-11-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_remove_checkout_status_remove_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartlist',
            name='status',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='status',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
