# Generated by Django 3.1.3 on 2020-11-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personapp', '0002_auto_20201128_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=1, verbose_name='age'),
            preserve_default=False,
        ),
    ]
