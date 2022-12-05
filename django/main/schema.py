import strawberry
from typing import List
from .types import Todo
from main.models import Todo as TodoModel

@strawberry.type
class Query:
    todos: List[Todo] = strawberry.django.field()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_todo(self, title: str) -> Todo:
        todo = TodoModel.objects.create(title=title)
        return todo

    @strawberry.mutation
    def delete_todo(self, id: int) -> bool:
        num_deleted, _ = TodoModel.objects.get(pk=id).delete()
        return num_deleted == 1

schema = strawberry.Schema(query=Query, mutation=Mutation)