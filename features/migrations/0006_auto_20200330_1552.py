# Generated by Django 2.2 on 2020-03-30 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_feature_contributors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='contributors',
            field=models.ManyToManyField(blank=True, related_name='feature_contributors', to=settings.AUTH_USER_MODEL),
        ),
    ]
