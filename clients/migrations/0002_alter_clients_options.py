# Generated by Django 3.2 on 2021-04-13 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'ordering': ['id']},
        ),
    ]
