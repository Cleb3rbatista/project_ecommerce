# Generated by Django 4.2.1 on 2023-05-26 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_alter_usuarios_nome_alter_usuarios_sobrenome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='senha',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='cep',
            field=models.IntegerField(default=00000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='id_User',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='sexo',
            field=models.CharField(default='M', max_length=1),
            preserve_default=False,
        ),
    ]