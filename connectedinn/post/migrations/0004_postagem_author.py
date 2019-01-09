# Generated by Django 2.1.4 on 2019-01-03 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_remove_perfil_postagem'),
        ('post', '0003_remove_postagem_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='perfil.Perfil'),
        ),
    ]