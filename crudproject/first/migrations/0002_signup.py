# Generated by Django 4.2 on 2023-04-27 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='login_id', max_length=15)),
                ('password', models.CharField(db_column='password', max_length=20)),
            ],
        ),
    ]
