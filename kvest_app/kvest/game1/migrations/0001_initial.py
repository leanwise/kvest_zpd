# Generated by Django 2.2.5 on 2019-09-22 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Team name')),
                ('progress', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('finish', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Mission name')),
                ('img', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('zone', models.IntegerField()),
                ('step', models.IntegerField()),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game1.Team')),
            ],
        ),
    ]
