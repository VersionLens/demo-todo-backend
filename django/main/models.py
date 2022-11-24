from django.db import models as m

class Todo(m.Model):
    title = m.CharField(max_length=128)

    def __str__(self):
        return self.title