# Generated by Django 4.1.7 on 2023-04-01 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcargas', '0007_alter_personas_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='apellido',
            field=models.CharField(blank=True, default='no especificado', max_length=12),
        ),
        migrations.AlterField(
            model_name='personas',
            name='nombre',
            field=models.CharField(blank=True, default='no especificado', max_length=11),
        ),
    ]
