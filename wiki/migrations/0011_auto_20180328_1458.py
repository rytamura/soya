# Generated by Django 2.0.3 on 2018-03-28 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0010_auto_20180309_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='image',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
