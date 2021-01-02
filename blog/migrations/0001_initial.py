# Generated by Django 2.2.2 on 2019-06-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField()),
                ('date_created', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('category', models.ManyToManyField(blank=True, to='blog.Category', verbose_name='Category Tag')),
            ],
            options={
                'ordering': ['date_published', 'date_created'],
            },
        ),
    ]
