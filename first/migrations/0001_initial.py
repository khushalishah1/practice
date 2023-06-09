# Generated by Django 4.2 on 2023-05-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insertproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(db_column='product_name', max_length=30)),
                ('pdescription', models.CharField(db_column='product_description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='login_id', max_length=15)),
                ('password', models.CharField(db_column='password', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='login_id', max_length=15)),
                ('password1', models.CharField(db_column='password', default=None, max_length=20)),
            ],
        ),
    ]
