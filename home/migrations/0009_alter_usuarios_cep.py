# Generated by Django 4.2.1 on 2023-05-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_usuarios_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cep',
            field=models.IntegerField(default=0),
        ),
    ]
