# Generated by Django 3.2.12 on 2024-07-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='payment_type',
            field=models.CharField(choices=[('ONLINE', 'ONLINE'), ('COD', 'COD')], max_length=50, null=True),
        ),
    ]