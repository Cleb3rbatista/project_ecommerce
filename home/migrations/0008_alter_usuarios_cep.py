# Generated by Django 4.2.1 on 2023-05-26 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_usuarios_senha_usuarios_cep_usuarios_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cep',
            field=models.IntegerField(blank=True),
        ),
    ]
