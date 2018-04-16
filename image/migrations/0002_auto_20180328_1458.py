# Generated by Django 2.0.3 on 2018-03-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='desc',
            field=models.CharField(default='description', max_length=256, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='image',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='緯度'),
        ),
        migrations.AddField(
            model_name='image',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='経度'),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='image title', max_length=64, verbose_name='名前'),
        ),
    ]