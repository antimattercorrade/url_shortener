from django.core.management.base import BaseCommand, CommandError
from shortener.models import Short_enURL

class Command(BaseCommand):
	help= 'Refreshes all Short_enURL shortcodes'

	def add_arguments(self,parser):
		parser.add_argument('--items',type=int)

	def handle(self,*args,**options):
		return Short_enURL.objects.refresh_shortcodes(items=options['items'])