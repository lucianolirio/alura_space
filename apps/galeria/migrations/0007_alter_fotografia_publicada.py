# Generated by Django 4.2 on 2023-04-18 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]
