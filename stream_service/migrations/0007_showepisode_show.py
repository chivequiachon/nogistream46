# Generated by Django 2.2.6 on 2019-11-01 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream_service', '0006_auto_20191028_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='showepisode',
            name='show',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='stream_service.ShowInfo'),
        ),
    ]