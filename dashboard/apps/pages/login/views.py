from django.views import generic
from dashboard.apps.core.utils import log


class IndexView(generic.TemplateView):
	"""
	IndexView:
	"""
	module = 'IndexView'
	template_name = 'login/base.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
