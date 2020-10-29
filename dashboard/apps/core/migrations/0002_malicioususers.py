# Generated by Django 3.0.3 on 2020-10-29 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0013_auto_20201029_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaliciousUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 6, 1, 0, 0))),
                ('hs_freq', models.IntegerField()),
                ('postfreq', models.IntegerField()),
                ('hsratio', models.IntegerField()),
                ('av_overperforming', models.IntegerField()),
                ('degree_centrality', models.IntegerField()),
                ('betweenness_centrality', models.IntegerField()),
                ('eigenvector_centrality', models.IntegerField()),
                ('pagerank', models.IntegerField()),
                ('malicious_score', models.IntegerField()),
            ],
        ),
    ]
