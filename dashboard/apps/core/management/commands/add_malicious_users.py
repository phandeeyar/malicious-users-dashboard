from django.core.management.base import BaseCommand
from dashboard.apps.core.models import MaliciousUsers
import pandas as pd
from datetime import datetime
from django.utils import timezone


def csv_to_model(path='dashboard/apps/core/management/commands/malicioususers.csv'):
	# TODO: make this path dynamic
	tmp_data = pd.read_csv(path, sep=',')
	users = []
	for index in tmp_data.index:
		users.append(MaliciousUsers(
			user_id=tmp_data['user_id'][index],
			hs_freq=tmp_data['hs_freq'][index],
			postfreq=tmp_data['postfreq'][index],
			hsratio=tmp_data['hsratio'][index],
			av_overperforming=tmp_data['av_overperforming'][index],
			degree_centrality=tmp_data['degree_centrality'][index],
			betweenness_centrality=tmp_data['betweenness_centrality'][index],
			eigenvector_centrality=tmp_data['eigenvector_centrality'][index],
			pagerank=tmp_data['pagerank'][index],
			malicious_score=tmp_data['malicious_score'][index],
			date=datetime(2020, 6, 2, tzinfo=timezone.utc) # TODO: Use this once @Anna adds date column 
		))
	MaliciousUsers.objects.bulk_create(users)


class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		csv_to_model()
