# Generated by Django 3.1.6 on 2021-03-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0059_remove_usuariodisciplina_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='titulo',
            field=models.CharField(max_length=25, verbose_name='Título'),
        ),
    ]
