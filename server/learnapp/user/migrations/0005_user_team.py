# Generated by Django 3.0.5 on 2020-05-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200509_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ManyToManyField(related_name='user_set', to='user.TeamRole'),
        ),
    ]
