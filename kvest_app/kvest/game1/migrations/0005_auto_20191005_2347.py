# Generated by Django 2.2.5 on 2019-10-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0004_auto_20191005_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='finish',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='start',
            field=models.TimeField(),
        ),
    ]
