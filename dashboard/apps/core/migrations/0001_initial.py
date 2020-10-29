# Generated by Django 3.0.3 on 2020-10-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataWindow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_url', models.CharField(max_length=100)),
                ('comment_id', models.CharField(max_length=100)),
                ('reply_id', models.CharField(max_length=100)),
                ('profile_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('likes', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('post_type', models.CharField(max_length=100)),
                ('row_id', models.CharField(max_length=100)),
                ('hate_speech', models.CharField(max_length=100)),
                ('page_name', models.CharField(max_length=100)),
                ('page_user_name', models.CharField(max_length=100)),
                ('page_likes_at_posting', models.CharField(max_length=100)),
                ('media_type', models.CharField(max_length=100)),
                ('post_likes', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=100)),
                ('shares', models.CharField(max_length=100)),
                ('angry_reactions', models.CharField(max_length=100)),
                ('media_link', models.CharField(max_length=100)),
                ('overperforming_score', models.CharField(max_length=100)),
                ('hate_speech_item1', models.CharField(max_length=100)),
                ('hate_speech_item2', models.CharField(max_length=100)),
                ('hate_speech_item3', models.CharField(max_length=100)),
                ('hate_speech_item4', models.CharField(max_length=100)),
                ('targeted_group1', models.CharField(max_length=100)),
                ('targeted_group2', models.CharField(max_length=100)),
                ('targeted_group3', models.CharField(max_length=100)),
                ('targeted_group4', models.CharField(max_length=100)),
                ('election_topic_hs', models.CharField(max_length=100)),
                ('number_of_posts', models.CharField(max_length=100)),
                ('election_topic', models.CharField(max_length=100)),
                ('election_topic_keyword', models.CharField(max_length=100)),
                ('double_comment', models.CharField(max_length=100)),
            ],
        ),
    ]
