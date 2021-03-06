# Generated by Django 3.1.6 on 2021-02-15 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0013_auto_20210214_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='usuarios',
            field=models.ManyToManyField(to='disciplina.Usuario'),
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.AddField(
            model_name='usuariodisciplina',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linguagem', to='disciplina.disciplina'),
        ),
        migrations.AddField(
            model_name='usuariodisciplina',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linguagem', to='disciplina.usuario'),
        ),
    ]
