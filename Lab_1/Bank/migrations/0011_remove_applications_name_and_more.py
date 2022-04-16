# Generated by Django 4.0.4 on 2022-04-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0010_applications_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='name',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='password',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='USERNAME_FIELD',
        ),
        migrations.RemoveField(
            model_name='company',
            name='USERNAME_FIELD',
        ),
        migrations.AddField(
            model_name='applications',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='bank',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='applications',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]
