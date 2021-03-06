# Generated by Django 3.2.5 on 2022-06-18 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wordsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='memory',
            field=models.BooleanField(default=False, verbose_name='暗記済み'),
        ),
        migrations.AlterField(
            model_name='post',
            name='answer',
            field=models.CharField(max_length=50, verbose_name='意味'),
        ),
        migrations.AlterField(
            model_name='post',
            name='question',
            field=models.CharField(max_length=20, verbose_name='英単語'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
