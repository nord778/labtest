# Generated by Django 3.1.3 on 2020-11-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Vin')),
                ('adress', models.CharField(db_index=True, max_length=64, verbose_name='adress')),
                ('work', models.CharField(db_index=True, max_length=64, verbose_name='work')),
            ],
        ),
    ]
