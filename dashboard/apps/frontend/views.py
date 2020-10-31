from django.shortcuts import render
from django.views import generic

from datetime import date, timedelta
from dashboard.apps.core.models import DataWindow, MaliciousUser, WordCloud, TargetGroup
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize


class IndexView(generic.ListView):
	""""
    IndexView:
    """

	module = 'indexView'
	template_name = 'frontend/index.html'

	def get_queryset(self):
		start_date = self.request.GET.get("start_date", date.today() - timedelta(days=7))
		end_date = self.request.GET.get("end_date", date.today())
		return DataWindow.objects.filter(date__gte=start_date, date__lte=end_date)

	def get_malicious_users(self):
		start_date = self.request.GET.get("start_date", date.today() - timedelta(days=7))
		end_date = self.request.GET.get("end_date", date.today())
		return MaliciousUser.objects.filter(date__gte=start_date, date__lte=end_date)
	
	def get_target_group_data(self):
		start_date = self.request.GET.get("start_date", date.today() - timedelta(days=7))
		end_date = self.request.GET.get("end_date", date.today())
		return TargetGroup.objects.filter(date__gte=start_date, date__lte=end_date)

	def get_word_cloud_data(self):
		start_date = self.request.GET.get("start_date", date.today() - timedelta(days=7))
		end_date = self.request.GET.get("end_date", date.today())
		return WordCloud.objects.filter(date__gte=start_date, date__lte=end_date)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		queryset = self.get_queryset()
		malicious_users_queryset = self.get_malicious_users()
		# Word Cloud Data
		context['word_cloud_data'] = serialize('json', self.get_word_cloud_data(), cls=DjangoJSONEncoder)
		top_20_malicious_users = malicious_users_queryset.order_by('-malicious_score')[:20]
		# Serialize data and send in context
		top_20_malicious_users = serialize('json', top_20_malicious_users, cls=DjangoJSONEncoder)
		context['top_20_malicious_users'] = top_20_malicious_users
		# number of posts in the selected date range
		context['number_of_posts'] = len(queryset.distinct('post_url'))
		# Number of comments in the selected date range
		context['number_of_comments'] = len(queryset)
		try:
			context['hate_speech_percent'] = (len(queryset.filter(hate_speech=True)) / len(queryset) * 100)
		except ZeroDivisionError:
			context['hate_speech_percent'] = 0
		context['targeted_groups_data'] = self.get_target_group_data()
		context['num_unique_users'] = len(queryset.distinct('profile_id'))

		return context
