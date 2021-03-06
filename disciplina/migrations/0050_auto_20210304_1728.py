# Generated by Django 3.1.6 on 2021-03-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0049_auto_20210304_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodisciplina',
            name='status',
            field=models.IntegerField(blank=True, choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=10, verbose_name='Situação'),
        ),
    ]
