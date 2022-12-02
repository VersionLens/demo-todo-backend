from django.core.management.base import BaseCommand

from main.models import Todo

class Command(BaseCommand):
    help = "Creates initial Todo models"
    
    def handle(self, *args, **options):
        Todo.objects.bulk_create([
            Todo(title="Buy milk"),
            Todo(title="Buy eggs"),
            Todo(title="Buy bread"),
        ])

        self.stdout.write(self.style.SUCCESS("Successfully created initial Todo models"))
