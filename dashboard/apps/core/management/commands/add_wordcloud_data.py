from django.core.management.base import BaseCommand
from dashboard.apps.core.models import WordCloud
import pandas as pd
from datetime import datetime
from django.utils import timezone


def csv_to_model(path='dashboard/apps/core/management/commands/wordcloud_w1.csv'):
	# TODO: make this path dynamic
	tmp_data = pd.read_csv(path, sep=',')
	users = []
	for index in tmp_data.index:
		users.append(WordCloud(
			word=tmp_data['word'][index],
			count=tmp_data['count'][index],
		))
	WordCloud.objects.bulk_create(users)


class Command(BaseCommand):
	help = 'Takes in wordcloud data from CSV and adds it to DB'

	def handle(self, *args, **kwargs):
		csv_to_model()
