# Generated by Django 2.2 on 2020-04-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_bug_when_resolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
