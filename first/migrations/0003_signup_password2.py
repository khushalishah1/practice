# Generated by Django 4.2 on 2023-05-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_signup_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password2',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
