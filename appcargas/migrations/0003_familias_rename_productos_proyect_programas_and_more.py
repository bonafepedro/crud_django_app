# Generated by Django 4.1.7 on 2023-04-01 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcargas', '0002_personas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='proyect',
            old_name='productos',
            new_name='programas',
        ),
        migrations.CreateModel(
            name='Ayudas_econ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField(max_length=8)),
                ('fecha', models.DateField()),
                ('id_beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcargas.personas')),
                ('id_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcargas.proyect')),
            ],
        ),
        migrations.AddField(
            model_name='personas',
            name='grupo_familiar',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appcargas.familias'),
            preserve_default=False,
        ),
    ]
