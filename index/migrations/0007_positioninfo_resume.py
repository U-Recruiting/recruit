# Generated by Django 2.1.2 on 2018-11-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20181109_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='positioninfo',
            name='resume',
            field=models.ManyToManyField(to='index.Resume'),
        ),
    ]
