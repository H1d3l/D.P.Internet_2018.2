# Generated by Django 2.1.5 on 2019-01-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0013_auto_20190127_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotoperfil/'),
        ),
    ]