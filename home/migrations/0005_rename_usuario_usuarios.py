# Generated by Django 4.2.1 on 2023-05-21 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_user_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuario',
            new_name='usuarios',
        ),
    ]
