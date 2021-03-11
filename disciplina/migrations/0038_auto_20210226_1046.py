# Generated by Django 3.1.6 on 2021-02-26 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disciplina', '0037_auto_20210225_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.OneToOneField(default=-1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Usuário'),
            preserve_default=False,
        ),
    ]