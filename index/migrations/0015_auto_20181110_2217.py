# Generated by Django 2.1.2 on 2018-11-10 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20181110_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionResumeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=20, verbose_name='状态')),
            ],
        ),
        migrations.AddField(
            model_name='positioninfo',
            name='org',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='index.OrgInfo'),
        ),
        migrations.AddField(
            model_name='positionresumestatus',
            name='position',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='index.PositionInfo'),
        ),
        migrations.AddField(
            model_name='positionresumestatus',
            name='resume',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='index.Resume'),
        ),
    ]
