# Generated by Django 2.1.3 on 2018-11-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181129_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='biography',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
