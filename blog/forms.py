__author__ = 'ekaradon'
import autocomplete_light
from blog.models import Entry


class EntryForm(autocomplete_light.ModelForm):
	class Meta:
		model = Entry
		autocomplete_fields = ('language',)
		fields = "__all__"
