# Generated by Django 2.0.5 on 2018-07-08 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0014_auto_20180708_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='name_church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Church', verbose_name='Nombre de iglesia'),
        ),
    ]
