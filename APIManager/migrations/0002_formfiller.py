# Generated by Django 3.0.3 on 2022-02-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFiller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('formData', models.CharField(default='m', max_length=10000)),
            ],
        ),
    ]
