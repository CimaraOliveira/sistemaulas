# Generated by Django 3.1.6 on 2021-03-06 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0057_usuariodisciplina_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodisciplina',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor', to='disciplina.professor'),
        ),
    ]
