# Generated by Django 3.2 on 2021-04-13 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquetes',
            name='numeroPaquete',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]