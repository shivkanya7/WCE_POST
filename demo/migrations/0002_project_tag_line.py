# Generated by Django 3.2 on 2021-04-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tag_line',
            field=models.CharField(default='', max_length=100),
        ),
    ]