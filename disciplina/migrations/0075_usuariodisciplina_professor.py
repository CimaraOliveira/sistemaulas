# Generated by Django 3.1.6 on 2021-03-15 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0074_remove_usuariodisciplina_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariodisciplina',
            name='professor',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='Professor', to='disciplina.professor'),
            preserve_default=False,
        ),
    ]