# Generated by Django 2.0.2 on 2018-02-17 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_feature'),
        ('wiki', '0003_auto_20180216_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='soya_certified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='image',
            name='landmark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='geo.Feature'),
        ),
        migrations.AddField(
            model_name='image',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='summary',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='wiki.Article'),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='wiki.Category'),
        ),
    ]