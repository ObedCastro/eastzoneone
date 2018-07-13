# Generated by Django 2.0.5 on 2018-07-12 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_church_pastor'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Distrito')),
            ],
            options={
                'verbose_name_plural': 'Distritos',
                'verbose_name': 'Distrito',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='church',
            name='content',
        ),
        migrations.RemoveField(
            model_name='church',
            name='image',
        ),
        migrations.AddField(
            model_name='church',
            name='region',
            field=models.CharField(blank=True, choices=[('Usulután', 'Usulután'), ('Ciudad Barrios', 'Ciudad Barrios'), ('San Miguel', 'San Miguel')], default='M', max_length=25, verbose_name='Región'),
        ),
        migrations.AddField(
            model_name='church',
            name='district',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='church.District', verbose_name='Distrito'),
            preserve_default=False,
        ),
    ]