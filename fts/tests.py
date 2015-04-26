from django.test import TestCase
from core.models import Language
from django.db.utils import IntegrityError
from django.core.management import call_command
from django.db import transaction

# Create your tests here.
class LanguageTestCase(TestCase):
	def setUp(self):
		call_command('populatedb')

	def test_languages_exist(self):
		count_entries = Language.objects.count()
		self.assertGreater(count_entries, 1, "There is more than one entries, counted: " + str(count_entries))

	def test_cannot_insert_existing_language(self):
		french = Language(name="french", locale="fr")
		error_occured = False
		try:
			with transaction.atomic():
				french.save()
		except IntegrityError:
			error_occured = True
		self.assertTrue(error_occured, "French already exists and cannot be added")

	def test_new_language_is_capitalized(self):
		dothraki = Language(name="dothraki", locale="GOT-dothraki")
		try:
			with transaction.atomic():
				dothraki.save()
		except Exception as inst:
			print(type(inst))    # the exception instance
			print(inst.args)     # arguments stored in .args
			print(inst)          # __str__ allows args to be printed directly,
		self.assertEqual(dothraki.name, "Dothraki", "Language must be capitalize")
		self.assertEqual(dothraki.locale, "GOT-dothraki", "Locale must not be changed")
