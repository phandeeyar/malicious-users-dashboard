from django.db import models
from datetime import datetime


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


class MaliciousUsers(models.Model):
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
