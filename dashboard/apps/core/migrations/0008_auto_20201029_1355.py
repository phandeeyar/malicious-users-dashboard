# Generated by Django 3.0.3 on 2020-10-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201029_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datawindow',
            name='double_comment',
            field=models.BooleanField(),
        ),
    ]
