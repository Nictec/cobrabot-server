# Generated by Django 2.2.6 on 2019-12-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0005_command_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='command',
            name='mod_only',
            field=models.BooleanField(default=False),
        ),
    ]