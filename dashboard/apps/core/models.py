from django.db import models
from datetime import datetime, timezone


# Create your models here.
class DataWindow(models.Model):
	post_url = models.TextField()
	comment_id = models.TextField()
	reply_id = models.TextField()
	profile_id = models.BigIntegerField()
	user_name = models.TextField()
	date = models.DateTimeField()
	comment = models.TextField()
	likes = models.IntegerField()
	user_id = models.TextField()
	post_type = models.TextField()
	row_id = models.TextField()
	hate_speech = models.BooleanField()
	page_name = models.TextField()
	page_user_name = models.TextField()
	page_likes_at_posting = models.TextField()
	media_type = models.TextField()
	post_likes = models.TextField()
	comments = models.TextField()
	shares = models.TextField()
	angry_reactions = models.IntegerField()
	media_link = models.TextField()
	overperforming_score = models.FloatField()
	hate_speech_item1 = models.TextField()
	hate_speech_item2 = models.TextField()
	hate_speech_item3 = models.TextField()
	hate_speech_item4 = models.TextField()
	targeted_group1 = models.TextField()
	targeted_group2 = models.TextField()
	targeted_group3 = models.TextField()
	targeted_group4 = models.TextField()
	election_topic_hs = models.BooleanField()
	number_of_posts = models.IntegerField()
	election_topic = models.BooleanField()
	election_topic_keyword = models.BooleanField()
	double_comment = models.BooleanField()

	def __str__(self):
		return 'Comment ID: {comment_id} by {user_id}'.format(comment_id=self.comment_id, user_id=self.user_id)


class MaliciousUser(models.Model):
	class Meta:
		indexes = [
			models.Index(fields=['user_id', 'hs_freq', 'malicious_score']),
			models.Index(fields=['user_id'], name='user_id_idx'),
			models.Index(fields=['malicious_score'], name='malicious_score_idx'),
		]

	user_id = models.CharField(max_length=200)
	hs_freq = models.IntegerField()
	postfreq = models.IntegerField()
	hsratio = models.IntegerField()
	av_overperforming = models.IntegerField()
	degree_centrality = models.IntegerField()
	betweenness_centrality = models.IntegerField()
	eigenvector_centrality = models.IntegerField()
	pagerank = models.IntegerField()
	malicious_score = models.IntegerField()
	date = models.DateTimeField(
		default=datetime(2020, 6, 1)
		# TODO: Change this to be now, did this to make it in sync with the rest of the data
	)

	def __str__(self):
		return self.user_id


class WordCloud(models.Model):
	word = models.CharField(max_length=100)
	count = models.IntegerField()
	date = models.DateTimeField(
		default=datetime(2020, 6, 1, tzinfo=timezone.utc)
		# TODO: Change this to be now, did this to make it in sync with the rest of the data
	)

	def __str__(self):
		return 'Word: {word} for dates: {date}'.format(word=self.word, date=self.date)


class TargetGroup(models.Model):
	group = models.CharField(max_length=100)
	count = models.IntegerField()
	percentage = models.DecimalField(
		decimal_places=6,
		max_digits=10
	)
	date = models.DateTimeField(
		default=datetime(2020, 6, 1, tzinfo=timezone.utc)
		# TODO: Change this to be now, did this to make it in sync with the rest of the data
	)

	def __str__(self):
		return 'Group: {group} was mentioned {count} times during dates: {date} '.format(
			group=self.group,
			date=self.date,
			count=self.count
		)
