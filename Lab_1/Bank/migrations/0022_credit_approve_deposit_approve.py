# Generated by Django 4.0.4 on 2022-04-18 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0021_rename_sum_transaction_sending_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='approve',
            field=models.CharField(choices=[('denied', 'denied'), ('checking', 'checking'), ('accepted', 'accepted')], default='checking', max_length=30),
        ),
        migrations.AddField(
            model_name='deposit',
            name='approve',
            field=models.CharField(choices=[('denied', 'denied'), ('checking', 'checking'), ('accepted', 'accepted')], default='checking', max_length=30),
        ),
    ]
