# Generated by Django 4.2 on 2023-04-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
        migrations.AddField(
            model_name='signup',
            name='password1',
            field=models.CharField(db_column='password', default=None, max_length=20),
        ),
    ]
