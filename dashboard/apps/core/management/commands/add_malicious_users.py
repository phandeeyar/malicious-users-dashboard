from django.core.management.base import BaseCommand
from dashboard.apps.core.models import MaliciousUser
import pandas as pd
from datetime import datetime
from dashboard.apps.core.utils import log


def csv_to_model(path='dashboard/apps/core/management/commands/malicioususers.csv'):
	# TODO: make this path dynamic
	tmp_data = pd.read_csv(path, sep=',')
	users = []
	for index in tmp_data.index:
		date = None
		try:
			date = tmp_data['date'][index]
		except KeyError:
			log("csv_to_model", 'csv_to_model', "couldn't get date", file=__file__)
		finally:
			if date is not None:
				users.append(MaliciousUser(
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
					date=datetime.fromisoformat(date),
				))
			else:
				users.append(MaliciousUser(
					user_id=tmp_data['user_id'][index],
					hs_freq=tmp_data['hs_freq'][index],
					postfreq=tmp_data['postfreq'][index],
					hsratio=tmp_data['hsratio'][index],
					av_overperforming=tmp_data['av_overperforming'][index],
					degree_centrality=tmp_data['degree_centrality'][index],
					betweenness_centrality=tmp_data['betweenness_centrality'][index],
					eigenvector_centrality=tmp_data['eigenvector_centrality'][index],
					pagerank=tmp_data['pagerank'][index],
					malicious_score=tmp_data['malicious_score'][index]
				))
	MaliciousUser.objects.bulk_create(users)


class Command(BaseCommand):
	help = 'Takes in malicious users from CSV and adds them to DB'

	# TODO: take in file path as an argument
	def handle(self, *args, **kwargs):
		csv_to_model()
