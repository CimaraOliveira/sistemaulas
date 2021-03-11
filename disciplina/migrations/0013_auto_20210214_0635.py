# Generated by Django 3.1.6 on 2021-02-14 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disciplina', '0012_auto_20210213_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='disciplina',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to='disciplina.disciplina'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to=settings.AUTH_USER_MODEL),
        ),
    ]
