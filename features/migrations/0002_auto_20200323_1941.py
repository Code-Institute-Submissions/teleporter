# Generated by Django 2.2 on 2020-03-23 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='category',
            field=models.CharField(blank=True, default='User-Requested', max_length=16),
        ),
        migrations.AddField(
            model_name='feature',
            name='price',
            field=models.DecimalField(decimal_places=2, default=50.0, max_digits=6),
        ),
    ]