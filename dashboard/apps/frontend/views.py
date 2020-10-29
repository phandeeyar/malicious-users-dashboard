from django.shortcuts import render
from django.views import generic

from datetime import date, timedelta
from dashboard.apps.core.utils import log
from dashboard.apps.core.models import DataWindow, MaliciousUsers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

class IndexView(generic.ListView):
	""""
    IndexView:
    """

	module = 'indexView'
	template_name = 'frontend/index.html'

	data = [
		['#', 'Header', 'Header', 'Header', 'Header'],
		['1,001', 'Lorem', 'ipsum', 'dolor', 'sit'],
		['1,002', 'amet', 'consectetur', 'adipiscing', 'elit'],
		['1,003', 'Integer', 'nec', 'odio', 'Praesent'],
		['1,003', 'libero', 'Sed', 'cursus', 'ante'],
		['1,004', 'dapibus', 'diam', 'Sed', 'nisi'],
		['1,005', 'Nulla', 'quis', 'sem', 'at'],
		['1,006', 'nibh', 'elementum', 'imperdit', 'Duis'],
		['1,007', 'sagittis', 'ipsum', 'Praesent', 'mauris'],
		['1,008', 'Fusce', 'nec', 'tellus', 'sed'],
		['1,009', 'augue', 'semper', 'porta', 'Mauris'],
		['1,010', 'massa', 'Vestibulum', 'lacinia', 'arcu'],
		['1,011', 'eget', 'nulla', 'Class', 'aptent'],
		['1,012', 'taciti', 'sociosqu', 'ad', 'litora'],
		['1,013', 'torquent', 'per', 'conubia', 'nostra'],
		['1,014', 'per', 'inceptos', 'himenaeos', 'Curabtur'],
		['1,015', 'sodales', 'ligula', 'in', 'libero'],
	]

	projects_original = [
		['Server Migration', '20%', 'bg-danger', '20'],
		['Sales Tracking', '40%', 'bg-warning', '40'],
		['Customer Database', '60%', '', '60'],
		['Payout Details', '80%', 'bg-info', '80'],
		['Account Setup', 'Complete!', 'bg-success', '100']
	]

	projects = [
		['Server Migration', '10%', 'bg-danger', '20'],
		['Sales Tracking', '70%', 'bg-info', '40'],
		['Customer Database', '60%', '', '60'],
		['Payout Details', 'Complete!', 'bg-success', '100'],
		['Account Setup', '40%', 'bg-warning', '40']
	]

	earnings_monthly = '$40.000'
	earnings_annual = '$250.000'
	task_percent = '75%'
	pending_requests = 18

	def get_queryset(self):
		log(self.module, 'get_queryset', file=__file__)
		start_date = self.request.GET.get("start_date", date.today() - timedelta(days=7))
		end_date = self.request.GET.get("end_date", date.today())
		return DataWindow.objects.filter(date__gte=start_date, date__lte=end_date)
	
	def get_malicious_users(self):
		start_date = self.request.GET.get("start_date", date.today() - timedelta(days=7))
		end_date = self.request.GET.get("end_date", date.today())
		return MaliciousUsers.objects.filter(date__gte=start_date, date__lte=end_date)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		queryset = self.get_queryset()
		malicious_users_queryset = self.get_malicious_users()
		top_20_malicious_users = malicious_users_queryset.order_by('-malicious_score')[:20]
		top_20_malicious_users = serialize('json', top_20_malicious_users, cls=DjangoJSONEncoder)
		context['top_20_malicious_users'] = top_20_malicious_users
		context['number_of_posts'] = len(queryset.distinct('post_url'))
		context['number_of_comments'] = len(queryset)
		try:
			context['hate_speech_percent'] = (len(queryset.filter(hate_speech=True)) / len(queryset) * 100)
		except ZeroDivisionError:
			context['hate_speech_percent'] = 0
		
		context['num_unique_users'] = len(queryset.distinct('profile_id'))
		context['projects'] = self.projects

		# log(self.module, 'get_context_data', 'context=%r' % context, file = __file__)

		return context
