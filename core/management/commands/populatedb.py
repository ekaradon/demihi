__author__ = 'ekaradon'
from django.core.management.base import BaseCommand
from core.models import Language
import babel

class Command(BaseCommand):
	args = ''
	help = 'Will populate the database with data generated from babel'

	def _create_languages(self):
		english_locale = babel.Locale('en')
		for key in english_locale.languages:
			language = Language(name=english_locale.languages[key], locale=key)
			language.save()

	def handle(self, *args, **options):
		self._create_languages()
