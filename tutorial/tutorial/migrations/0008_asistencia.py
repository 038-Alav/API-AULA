# Generated by Django 4.2.7 on 2023-11-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0007_clases'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Alumno', models.CharField(max_length=30)),
                ('RUT_Alumno', models.CharField(max_length=100)),
            ],
        ),
    ]