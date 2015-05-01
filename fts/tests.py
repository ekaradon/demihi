from django.test import TestCase
from core.models import Language
from blog.models import Entry
from django.db.utils import IntegrityError
from django.core.management import call_command
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Count

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

class EntryTestCase(TestCase):
	def setUp(self):
		author = User(last_name="chocolate", email="chocolate@demihi.com")
		author.save()
		call_command('populatedb')
		entry_new = Entry(
			author=User.objects.get(pk=1),
			body='foo',
			language=Language.objects.get(pk=5),
			summary='bar',
			title='foo bar',
		)
		entry_new.save()
		entry_old = Entry(
			author=User.objects.get(pk=1),
			body='test',
			language=Language.objects.get(name="French"),
			summary='ceci est un résumé',
			title='Test de langue',
		)
		entry_old.save()

	def test_get_number_of_entries(self):
		count_entries = Entry.objects.count()
		self.assertEqual(2, count_entries, "Two entries have been declared")

	def test_number_languages_used(self):
		entries_aggregate = Entry.objects.aggregate(Count('language'))
		self.assertEqual(2, entries_aggregate['language__count'], "Two differents language have been used")

	def test_french_language_used(self):
		result = Entry.objects.get(language__name='French')
		self.assertIsNotNone(result, "An Entry must be found there")
