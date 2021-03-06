# Generated by Django 3.1.6 on 2021-02-16 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0017_remove_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodisciplina',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplina.disciplina'),
        ),
        migrations.AlterField(
            model_name='usuariodisciplina',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplina.usuario'),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovdo'), (2, 'Cancelado')], default=0, verbose_name='Situação')),
                ('dataReserva', models.DateTimeField(auto_now_add=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linguagem', to='disciplina.disciplina')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linguagem', to='disciplina.usuario')),
            ],
        ),
    ]
