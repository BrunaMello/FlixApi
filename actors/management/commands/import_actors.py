from django.core.management.base import BaseCommand


class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument(
			'file_name',
			type=int,
			help='The file name to import actors from'
		)
		parser.add_argument(
			'file_name2',
			type=int,
			help='The file name to import actors from'
		)

	def handle(self, *args, **options):
		file_name = options['file_name']
		file_name2 = options['file_name2']
		print(f'Command executed! {file_name}')
