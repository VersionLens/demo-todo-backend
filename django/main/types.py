import strawberry
from strawberry import auto
from typing import List
from . import models

@strawberry.django.type(models.Todo)
class Todo:
    id: auto
    title: auto
