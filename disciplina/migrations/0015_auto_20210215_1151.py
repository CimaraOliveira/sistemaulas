# Generated by Django 3.1.6 on 2021-02-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0014_auto_20210215_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='usuarios',
        ),
        migrations.AddField(
            model_name='usuariodisciplina',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=0, verbose_name='Situação'),
        ),
    ]
