# Generated by Django 2.0.6 on 2018-07-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='marked',
            field=models.IntegerField(default=0),
        ),
    ]
