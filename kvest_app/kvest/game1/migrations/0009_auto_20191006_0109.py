# Generated by Django 2.2.5 on 2019-10-05 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0008_auto_20191006_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game1.Team'),
        ),
    ]