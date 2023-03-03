from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create admin user'

    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--username',
            type=str,
            default='admin',
        )
        parser.add_argument(
            '-p',
            '--password',
            type=str,
            default='admin1234',
        )
        parser.add_argument(
            '-e',
            '--email',
            type=str,
        )

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        email = kwargs['email']

        if email:
            email = email
        else:
            email = f'{username}@example.com'

        if User.objects.filter(username=username):
            raise CommandError(f'Username `{username}` already taken.')
        if User.objects.filter(email=email):
            raise CommandError(f'Email `{email}` already taken.')

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )
    
        self.stdout.write(self.style.SUCCESS(f'Admin `{username}` successfully created!'))