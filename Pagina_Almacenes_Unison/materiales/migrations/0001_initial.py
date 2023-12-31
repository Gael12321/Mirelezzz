# Generated by Django 3.2.19 on 2023-11-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_articulo', models.CharField(max_length=50)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(choices=[('Electrico', 'Electrico'), ('Plomeria', 'Plomeria'), ('Limpieza', 'Limpieza'), ('Oficina', 'Oficina')], max_length=10)),
                ('cantidad', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='material/')),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad_limite', models.IntegerField()),
                ('Origen', models.CharField(choices=[('Unison', 'Unison'), ('Exterior', 'Exterior')], max_length=8)),
            ],
        ),
    ]
