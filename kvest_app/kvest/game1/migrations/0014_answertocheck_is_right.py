# Generated by Django 2.2.5 on 2019-10-05 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0013_answertocheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='answertocheck',
            name='is_right',
            field=models.BooleanField(default=None),
        ),
    ]