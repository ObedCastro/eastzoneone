# Generated by Django 2.0.5 on 2018-07-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_church_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='pastor',
            field=models.CharField(default=0, max_length=100, verbose_name='Pastor'),
            preserve_default=False,
        ),
    ]