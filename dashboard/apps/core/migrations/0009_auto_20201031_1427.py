# Generated by Django 3.0.3 on 2020-10-31 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_targetgroups'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TargetGroups',
            new_name='TargetGroup',
        ),
    ]
