# Generated by Django 2.1.3 on 2018-12-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_teammember_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='lastname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='biography',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='nickname',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
