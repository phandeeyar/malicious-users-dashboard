import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from dashboard.apps.core.models import DataWindow
from dashboard.apps.core.utils import log


def str_to_bool(s):
	if s == 'True':
		return True
	elif s == 'False':
		return False
	else:
		raise ValueError  # evil ValueError that doesn't tell you what the wrong value was


def str_to_int(num):
	if num is None or num == '':
		return 0
	else:
		return int(float(num))


def str_to_float(num):
	if num is None or num == '':
		return 0
	else:
		return float(num)


def _csv_to_model(path='dashboard/apps/core/management/commands/window(1).csv'):
	data_windows = []
	with open(path, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		next(csv_reader)
		for row in csv_reader:
			date = None
			try:
				date = row['date']
			except KeyError:
				log("csv_to_model", 'csv_to_model', "couldn't get date", file=__file__)
			finally:
				try:
					data_window = DataWindow(
						post_url=row['post_url'],
						reply_id=row['reply_id'],
						profile_id=str_to_int(row['profile_id']),
						user_name=row['user_name'],
						comment=row['comment'],
						likes=str_to_int(row['likes']),
						user_id=row['user_id'],
						post_type=row['post_type'],
						row_id=row['row_id'],
						hate_speech=str_to_bool(row['hate_speech']),
						page_name=row['page_name'],
						page_user_name=row['page_user_name'],
						page_likes_at_posting=str_to_int(row['page_likes_at_posting']),
						media_type=row['media_type'],
						post_likes=str_to_int(row['post_likes']),
						comments=str_to_int(row['comments']),
						shares=str_to_int(row['shares']),
						angry_reactions=str_to_int(row['angry_reactions']),
						media_link=row['media_link'],
						overperforming_score=str_to_float(row['overperforming_score']),
						hate_speech_item1=row['hate_speech_item1'],
						hate_speech_item2=row['hate_speech_item2'],
						hate_speech_item3=row['hate_speech_item3'],
						hate_speech_item4=row['hate_speech_item4'],
						targeted_group1=row['targeted_group1'],
						targeted_group2=row['targeted_group2'],
						targeted_group3=row['targeted_group3'],
						targeted_group4=row['targeted_group4'],
						election_topic_hs=str_to_bool(row['election_topic_hs']),
						number_of_posts=str_to_int(row['number_of_posts']),
						election_topic=str_to_bool(row['election_topic']),
						election_topic_keyword=str_to_bool(row['election_topic_keyword']),
						double_comment=str_to_bool(row['double_comment']),
					)
					if row['comment_id'] is not None and row['comment_id'] != '':
						data_window.comment_id = int(float(row['comment_id']))
					if date is not None and date != '':
						data_window.date = datetime.fromisoformat(date)
					data_windows.append(data_window)
				except Exception as e:
					log("csv_to_model", 'csv_to_model', e, file=__file__)
					raise
	DataWindow.objects.bulk_create(data_windows)


class Command(BaseCommand):
	help = 'Takes in data window from CSV and adds them to DB'

	# TODO: take in file path as an argument
	def handle(self, *args, **kwargs):
		_csv_to_model()
