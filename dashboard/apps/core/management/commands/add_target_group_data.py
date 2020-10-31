from django.core.management.base import BaseCommand
from dashboard.apps.core.models import TargetGroup
from datetime import datetime
import pandas as pd
from dashboard.apps.core.utils import log


def csv_to_model(path='dashboard/apps/core/management/commands/target_groups.csv'):
	tmp_data = pd.read_csv(path, sep=',')
	groups = []
	for index in tmp_data.index:
		date = None
		try:
			date = tmp_data['date'][index]
		except KeyError:
			log("csv_to_model", 'csv_to_model', "couldn't get date", file=__file__)
		finally:
			if date is not None:
				groups.append(TargetGroup(
					group=tmp_data['group'][index],
					count=tmp_data['count'][index],
					percentage=tmp_data['percentage'][index],
					# Needs to be ISO datetime
					date=datetime.fromisoformat(date),
				))
			else:
				log("csv_to_model", 'csv_to_model', "added without date {group}".format(group=tmp_data['group'][index]), file=__file__)
				groups.append(TargetGroup(
					group=tmp_data['group'][index],
					count=tmp_data['count'][index],
					percentage=tmp_data['percentage'][index]
				))
	TargetGroup.objects.bulk_create(groups)


class Command(BaseCommand):
	help = 'Takes in targeted group data from CSV and adds it to DB'
	# TODO: take in file path as an argument
	def handle(self, *args, **kwargs):
		csv_to_model()
