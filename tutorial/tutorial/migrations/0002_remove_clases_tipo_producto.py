# Generated by Django 4.2.3 on 2023-11-07 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clases',
            name='tipo_producto',
        ),
    ]
