# Generated by Django 4.0.4 on 2022-04-15 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0007_requests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Applications',
        ),
    ]
