from django.db import models

# Create your models here.

from shortener.models import Short_enURL


class ClickEventManager(models.Manager):
	def create_event(self,short_enInstance):
		if isinstance(short_enInstance, Short_enURL):
			obj, created = self.get_or_create(short_enurl=short_enInstance)
			obj.count+=1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	short_enurl = models.OneToOneField(Short_enURL, on_delete=models.CASCADE)
	count = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)
	