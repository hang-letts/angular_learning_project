# Generated by Django 2.1.2 on 2018-10-15 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accapp', '0003_auto_20181015_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginmodel',
            old_name='password',
            new_name='psswrd',
        ),
    ]
