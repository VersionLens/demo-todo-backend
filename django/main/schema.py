import strawberry
from typing import List
from .types import Todo

@strawberry.type
class Query:
    todos: List[Todo] = strawberry.django.field()

schema = strawberry.Schema(query=Query)