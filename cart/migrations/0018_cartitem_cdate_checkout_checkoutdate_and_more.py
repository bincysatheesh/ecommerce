# Generated by Django 4.2.4 on 2023-11-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_remove_cartlist_status_cartitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cdate',
            field=models.DateTimeField(default='2023-10-30'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='checkoutdate',
            field=models.DateTimeField(default='2023-10-30'),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentdate',
            field=models.DateTimeField(default='2023-10-30'),
        ),
        migrations.AlterField(
            model_name='cartlist',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
