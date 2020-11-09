from datetime import date, timedelta, datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.views import generic

from dashboard.apps.core.models import DataWindow, MaliciousUser, WordCloud, TargetGroup


class IndexView(LoginRequiredMixin, generic.base.TemplateView):
	""""
    IndexView:
    """

	module = 'indexView'
	template_name = 'frontend/index.html'

	@staticmethod
	def get_data_window_objects(date_range_lower, date_range_upper):
		return DataWindow.objects.filter(date__gte=date_range_lower, date__lte=date_range_upper)

	@staticmethod
	def get_malicious_users(date_range_lower, date_range_upper):
		return MaliciousUser.objects.filter(date__gte=date_range_lower, date__lte=date_range_upper)

	@staticmethod
	def get_target_group_data(date_range_lower, date_range_upper):
		return TargetGroup.objects.filter(date__gte=date_range_lower, date__lte=date_range_upper)

	@staticmethod
	def get_word_cloud_data(date_range_lower, date_range_upper):
		return WordCloud.objects.filter(date__gte=date_range_lower, date__lte=date_range_upper)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		dtl = self.request.GET.get("start_date", date.today() - timedelta(days=7))  # Upper Date Range
		if dtl == "":
			date_range_lower = date.today() - timedelta(days=7)
		else:
			date_range_lower = dtl

		# dtu = self.request.GET.get("end_date", date.today())  # Lower Date Range
		# if dtu == "":
		# 	date_range_upper = date.today()
		# else:
		# 	date_range_upper = dtu

		# set upper date range to be 7 days from start
		if isinstance(date_range_lower, date):
			date_range_upper = date_range_lower + timedelta(days=7)
		else:
			date_range_upper = datetime.strptime(date_range_lower, '%Y-%m-%d').date() + timedelta(days=7)
		context["start_date"] = str(date_range_lower)
		context["end_date"] = str(date_range_upper)
		data_window_queryset = self.get_data_window_objects(date_range_lower, date_range_upper)
		malicious_users_queryset = self.get_malicious_users(date_range_lower, date_range_upper)
		context['targeted_groups_data'] = self.get_target_group_data(date_range_lower, date_range_upper)
		# Word Cloud Data
		context['word_cloud_data'] = serialize('json', self.get_word_cloud_data(date_range_lower, date_range_upper),
											   cls=DjangoJSONEncoder)
		top_20_malicious_users = malicious_users_queryset.order_by('-malicious_score')[:20]
		# Serialize data and send in context
		top_20_malicious_users_ids = top_20_malicious_users.values_list('user_id', flat=True)
		comments_by_top_20_malicious_users = data_window_queryset.filter(
			user_id__in=top_20_malicious_users_ids)
		targeted_group_data = comments_by_top_20_malicious_users.exclude(targeted_group1__exact='').values(
			'user_id',
			'targeted_group1',
			'targeted_group2',
			'targeted_group3',
			'targeted_group4'
		)
		top_20_malicious_users = serialize('json', top_20_malicious_users, cls=DjangoJSONEncoder)
		context['top_20_malicious_users'] = top_20_malicious_users
		# number of posts in the selected date range
		context['number_of_posts'] = len(data_window_queryset.distinct('post_url'))
		# Number of comments in the selected date range
		context['number_of_comments'] = len(data_window_queryset)
		try:
			context['hate_speech_percent'] = (
				len(data_window_queryset.filter(hate_speech=True)) / len(data_window_queryset) * 100)
		except ZeroDivisionError:
			context['hate_speech_percent'] = 0

		context['num_unique_users'] = len(data_window_queryset.distinct('profile_id'))

		return context


class MethodologyView(LoginRequiredMixin, generic.base.TemplateView):
	module = 'MethodologyView'
	template_name = 'frontend/methodology.html'
