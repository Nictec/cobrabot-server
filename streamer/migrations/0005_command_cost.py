# Generated by Django 2.2.6 on 2019-12-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0004_auto_20191219_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
