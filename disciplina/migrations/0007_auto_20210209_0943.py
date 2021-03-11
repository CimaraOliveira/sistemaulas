# Generated by Django 3.1.6 on 2021-02-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0006_auto_20210208_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cpf',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default=-1.0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
