# Generated by Django 3.1.6 on 2021-02-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0038_auto_20210226_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
