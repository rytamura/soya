# Generated by Django 2.0.2 on 2018-02-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_auto_20180217_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='categories',
            field=models.ManyToManyField(to='wiki.Category'),
        ),
    ]