from django.core.management.base import BaseCommand
from dashboard.apps.core.models import WordCloud
import pandas as pd
from dashboard.apps.core.utils import log
from datetime import datetime


def csv_to_model(path='dashboard/apps/core/management/commands/wordcloud_w1.csv'):
	# TODO: make this path dynamic
	tmp_data = pd.read_csv(path, sep=',')
	users = []
	for index in tmp_data.index:
		date = None
		try:
			date = tmp_data['week'][index]
		except KeyError:
			log("csv_to_model", 'csv_to_model', "couldn't get date", file=__file__)
		finally:
			if date is not None:
				users.append(WordCloud(
					word=tmp_data['word'][index],
					count=tmp_data['count'][index],
					date=datetime.strptime(date, '%d/%m/%Y').date()
					# date=datetime.fromisoformat(date),
				))
			else:
				users.append(WordCloud(
					word=tmp_data['word'][index],
					count=tmp_data['count'][index],
				))
	WordCloud.objects.bulk_create(users)


class Command(BaseCommand):
	help = 'Takes in wordcloud data from CSV and adds it to DB'

	# TODO: take in file path as an argument
	def handle(self, *args, **kwargs):
		csv_to_model()
