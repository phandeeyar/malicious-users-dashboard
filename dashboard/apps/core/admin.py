from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from dashboard.apps.core.models import DataWindow, MaliciousUser, WordCloud, TargetGroup, Lexicon


class DataWindowResource(resources.ModelResource):
	class Meta:
		model = DataWindow


class DataWindowAdmin(ImportExportModelAdmin):
	resource_class = DataWindowResource


admin.site.register(DataWindow, DataWindowAdmin)
admin.site.register(MaliciousUser)
admin.site.register(WordCloud)
admin.site.register(TargetGroup)
admin.site.register(Lexicon)
