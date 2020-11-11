import pandas as pd
from django.core.management.base import BaseCommand

from dashboard.apps.core.models import Lexicon


def csv_to_model(path='dashboard/apps/core/management/commands/leixcons.csv'):
	tmp_data = pd.read_csv(path, sep=',')
	lexicons = []
	for index in tmp_data.index:
		lexicons.append(Lexicon(
			label=tmp_data['label'][index],
			meaning=tmp_data['meaning'][index],
			targetted_group=tmp_data['targetted_group'][index],
			type=tmp_data['type'][index],
			language=tmp_data['language'][index],
		))
	Lexicon.objects.bulk_create(lexicons)


class Command(BaseCommand):
	help = 'Takes in Lexicon data from CSV and adds it to DB'

	# TODO: take in file path as an argument
	def handle(self, *args, **kwargs):
		csv_to_model()
