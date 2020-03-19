# Generated by Django 2.2 on 2020-03-18 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0009_remove_vote_bug_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugcomment',
            name='votes',
            field=models.ManyToManyField(related_name='comment_votes', through='bugs.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vote',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bugs.BugComment'),
            preserve_default=False,
        ),
    ]
