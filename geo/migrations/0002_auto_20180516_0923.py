# Generated by Django 2.0.3 on 2018-05-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=128, verbose_name='場所の名前'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='note',
            field=models.CharField(max_length=256, verbose_name='市町村名'),
        ),
    ]
