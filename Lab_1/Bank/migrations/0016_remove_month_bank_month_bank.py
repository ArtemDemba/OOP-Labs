# Generated by Django 4.0.4 on 2022-04-16 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0015_interestrate_delete_credit_deposit_interest_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='month',
            name='bank',
        ),
        migrations.AddField(
            model_name='month',
            name='bank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Bank.bank'),
            preserve_default=False,
        ),
    ]
