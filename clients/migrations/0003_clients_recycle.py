# Generated by Django 3.2 on 2021-04-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_clients_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='Recycle',
            field=models.BooleanField(default=False),
        ),
    ]
