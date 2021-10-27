# Generated by Django 3.2.8 on 2021-10-25 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dimensiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creado', models.DateTimeField(auto_created=True, verbose_name='Fecha de creación')),
                ('rut', models.CharField(max_length=20, unique=True, verbose_name='Documento Chileno de identificación')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('fecha_editado', models.DateTimeField(auto_now=True, verbose_name='Fecha de Ultima Edición')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fondos.rol', verbose_name='Rol')),
            ],
        ),
        migrations.CreateModel(
            name='publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fondo', models.CharField(max_length=200, verbose_name='Nombre del Fondo')),
                ('objetivo', models.CharField(max_length=300, null=True, verbose_name='Objetivo')),
                ('enlace', models.CharField(max_length=200, verbose_name='Link')),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha inicio')),
                ('fecha_termino', models.DateTimeField(verbose_name='Fecha termino')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fondos.usuario', verbose_name='Autor')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fondos.dimensiones', verbose_name='Dimensión')),
            ],
        ),
        migrations.CreateModel(
            name='adjudicarse_fondo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fondos.estado')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fondos.publicaciones')),
                ('subscriptor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fondos.usuario')),
            ],
        ),
    ]
