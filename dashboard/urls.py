from django.contrib import admin

from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
import django.contrib.auth.views as auth_views

app_name = 'main'

urlpatterns = [
	path('', include('dashboard.apps.urls')),
	url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login/login.html'), name='login_url'),
	url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout_url'),
	path('admin/', admin.site.urls),
]
