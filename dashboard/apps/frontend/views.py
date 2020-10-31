from django.shortcuts import render
from django.views import generic
from django import forms
from datetime import date, timedelta
from dashboard.apps.core.models import DataWindow, MaliciousUser, WordCloud, TargetGroup
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin


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
		dtu = self.request.GET.get("end_date", date.today())  # Lower Date Range
		if dtu == "":
			date_range_upper = date.today()
		else:
			date_range_upper = dtu
		data_window_queryset = self.get_data_window_objects(date_range_lower, date_range_upper)
		malicious_users_queryset = self.get_malicious_users(date_range_lower, date_range_upper)
		context['targeted_groups_data'] = self.get_target_group_data(date_range_lower, date_range_upper)
		# Word Cloud Data
		context['word_cloud_data'] = serialize('json', self.get_word_cloud_data(date_range_lower, date_range_upper), cls=DjangoJSONEncoder)
		top_20_malicious_users = malicious_users_queryset.order_by('-malicious_score')[:20]
		# Serialize data and send in context
		top_20_malicious_users = serialize('json', top_20_malicious_users, cls=DjangoJSONEncoder)
		context['top_20_malicious_users'] = top_20_malicious_users
		# number of posts in the selected date range
		context['number_of_posts'] = len(data_window_queryset.distinct('post_url'))
		# Number of comments in the selected date range
		context['number_of_comments'] = len(data_window_queryset)
		try:
			context['hate_speech_percent'] = (len(data_window_queryset.filter(hate_speech=True)) / len(data_window_queryset) * 100)
		except ZeroDivisionError:
			context['hate_speech_percent'] = 0
		
		context['num_unique_users'] = len(data_window_queryset.distinct('profile_id'))

		return context