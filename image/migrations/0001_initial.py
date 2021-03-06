# Generated by Django 2.0.3 on 2018-05-15 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='作成日')),
                ('uploaded_at', models.DateTimeField(verbose_name='アップロード日')),
                ('title', models.CharField(default='image title', max_length=64, verbose_name='名前')),
                ('desc', models.CharField(default='description', max_length=256, verbose_name='説明')),
                ('longitude', models.FloatField(null=True, verbose_name='経度')),
                ('latitude', models.FloatField(null=True, verbose_name='緯度')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
