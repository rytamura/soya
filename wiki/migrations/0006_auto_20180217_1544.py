# Generated by Django 2.0.2 on 2018-02-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='soya_certified',
            field=models.BooleanField(default=False, help_text='Certified', verbose_name='認証済'),
        ),
    ]
