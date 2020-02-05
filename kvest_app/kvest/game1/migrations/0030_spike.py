# Generated by Django 2.2.5 on 2019-10-13 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game1', '0029_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game1.AnswerToCheck')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game1.Mission')),
            ],
        ),
    ]
