# Generated by Django 3.1.6 on 2021-02-16 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0016_usuario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
    ]
