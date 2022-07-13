from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from mimesis import Person

from mainapp.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=settings.ADMIN_USERNAME)
            user.delete()
        except User.DoesNotExist:
            print('Database is empty')
        User.objects.create_superuser(
            username=settings.ADMIN_USERNAME,
            email=settings.ADMIN_EMAIL,
            password=settings.ADMIN_PASSWORD
        )

        Student.objects.all().delete()
        quantity_students = 20
        person = Person('ru')
        for _ in range(quantity_students):
            Student.objects.create(
                firstname=person.first_name(),
                lastname=person.last_name(),
                email=person.email(),
                university=person.university()
            )
