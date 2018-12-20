# Generated by Django 2.1.3 on 2018-12-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_servico_servico'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComboServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='servico',
            name='servico',
        ),
        migrations.AddField(
            model_name='comboservico',
            name='servico',
            field=models.ManyToManyField(to='core.Servico'),
        ),
    ]