# Generated by Django 2.0.5 on 2018-07-07 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('church', '0003_church_pastor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reports', models.CharField(max_length=100, verbose_name='Quien reporta')),
                ('position', models.CharField(blank=True, choices=[('P', 'Presidente'), ('V', 'Vice_presidente'), ('S', 'Secretario'), ('T', 'Tesorero'), ('M', 'Miembro')], default='M', max_length=1, verbose_name='Cargo')),
                ('month', models.CharField(blank=True, choices=[('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio'), ('JUL', 'Julio'), ('AGO', 'Agosto'), ('SEP', 'Septiembre'), ('OCT', 'Octubre'), ('NOV', 'Noviembre'), ('DIC', 'Diciembre')], default='M', max_length=3, verbose_name='Mes')),
                ('category', models.CharField(blank=True, choices=[('D', 'Diezmo'), ('O', 'Ofrendas')], default='O', max_length=1, verbose_name='Categoría')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('name_church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Church', verbose_name='Nombre de iglesia')),
            ],
            options={
                'verbose_name': 'Finanza',
                'ordering': ['month'],
                'verbose_name_plural': 'Finanzas',
            },
        ),
    ]
