import datetime
import os

from django.db import models

from django.contrib.auth.models import User
from django.db.models import Model

from django.utils import timezone

from PIL import Image as PImage
from django.conf import settings
from core.models import Language


# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length=60)
	public = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title


class Comment(Model):
	answer_to = models.ForeignKey('self', blank=True, null=True)
	author = models.ForeignKey(User)
	body = models.TextField()
	entry = models.ForeignKey('Entry')
	date_modified = models.DateTimeField('last time modified', auto_now=True)
	date_published = models.DateTimeField('date published', auto_now_add=True)

	def __str__(self):
		return "Response to: " + self.entry.title


class Entry(Model):
	active = models.BooleanField('publish', default=False)
	author = models.ForeignKey(User)
	body = models.TextField()
	header = models.ForeignKey('Image', blank=True, null=True)
	language = models.ForeignKey(Language, db_index=True)
	date_modified = models.DateTimeField('last time modified', auto_now=True)
	date_published = models.DateTimeField('date published', editable=False, blank=True, null=True)
	date_created = models.DateTimeField('date created', auto_now_add=True)
	tags = models.ManyToManyField('Tag', blank=True)
	title = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.title

	def is_published(self):
		return self.active

	def was_published_recently(self):
		if self.date_published:
			return self.date_published >= timezone.now() - datetime.timedelta(days=1)
		return False

	def tags_(self):
		lst = [x[1] for x in self.tags.values_list()]
		return ', '.join(lst)

	def save(self, *args, **kwargs):
		if self.is_published() and not self.date_published :
			self.date_published = datetime.datetime.today()
		super(Entry, self).save(*args, ** kwargs)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Image(models.Model):
	title = models.CharField(max_length=60, blank=True, null=True)
	image = models.FileField(upload_to="upload/")
	tags = models.ManyToManyField('Tag', blank=True)
	albums = models.ManyToManyField(Album, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=50)
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	user = models.ForeignKey(User, null=True, blank=True)

	def __unicode__(self):
		return self.image.name

	def __str__(self):
		return self.image.name

	def save(self, *args, **kwargs):
		"""Save image dimensions."""
		super(Image, self).save(*args, **kwargs)
		im = PImage.open(os.path.join(settings.MEDIA_ROOT, self.image.name))
		self.width, self.height = im.size
		super(Image, self).save(*args, ** kwargs)

	def tags_(self):
		lst = [x[1] for x in self.tags.values_list()]
		return ', '.join(lst)

	def albums_(self):
		lst = [x[1] for x in self.albums.values_list()]
		return  ', '.join(lst)

	def size(self):
		"""Image size."""
		return "%s x %s" % (self.width, self.height)

	def thumbnail(self):
		return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
			(self.image.name, self.image.name)
		)
	thumbnail.allow_tags = True


class Tag(Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	def clean(self):
		self.name = self.name.lower()
