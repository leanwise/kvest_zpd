# Generated by Django 2.2.5 on 2019-10-05 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0011_auto_20191006_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='teama',
            new_name='team',
        ),
    ]
