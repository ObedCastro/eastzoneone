# Generated by Django 2.0.5 on 2018-07-08 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20180707_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='finance',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Cantidad $ '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finance',
            name='name_church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Church', verbose_name='Nombre de iglesia'),
        ),
    ]
