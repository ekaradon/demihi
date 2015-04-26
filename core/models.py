from django.db import models

# Create your models here.
class Language(models.Model):
	name = models.CharField(max_length=20, unique=True)
	locale = models.CharField(max_length=4)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.name = self.name.capitalize()
		super(Language, self).save(*args, **kwargs)