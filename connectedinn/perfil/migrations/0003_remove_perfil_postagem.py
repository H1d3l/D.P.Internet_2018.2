# Generated by Django 2.1.4 on 2019-01-03 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_perfil_postagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='postagem',
        ),
    ]