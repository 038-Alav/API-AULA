# Generated by Django 4.2.2 on 2023-11-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0008_asistencia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistencia',
            old_name='nombre_Alumno',
            new_name='nombreAlum',
        ),
        migrations.RenameField(
            model_name='asistencia',
            old_name='RUT_Alumno',
            new_name='rutAlum',
        ),
        migrations.AddField(
            model_name='alumno',
            name='apellidoM',
            field=models.CharField(default='no especificado', max_length=30),
        ),
        migrations.AddField(
            model_name='alumno',
            name='apellidoP',
            field=models.CharField(default='no especificado', max_length=30),
        ),
        migrations.AddField(
            model_name='alumno',
            name='contraseña',
            field=models.CharField(default='no especificado', max_length=20),
        ),
        migrations.AddField(
            model_name='alumno',
            name='correo',
            field=models.EmailField(default='no especificado', max_length=254),
        ),
        migrations.AddField(
            model_name='alumno',
            name='nomUsuario',
            field=models.CharField(default='no especificado', max_length=40),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(default='no especificado', max_length=30),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='rut',
            field=models.TextField(default='no especificado'),
        ),
    ]