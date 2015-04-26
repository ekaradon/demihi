from django.contrib import admin
from core.models import Language

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
	model = Language
	fieldsets = [
		('', {'fields': ['name', 'locale']})
	]
	list_display = ['name', 'locale']
	search_fields = ['name', 'locale']
	ordering = ('name',)

admin.site.register(Language, LanguageAdmin)