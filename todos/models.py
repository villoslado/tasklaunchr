from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    task = models.CharField(max_length=255)
    todolist = models.ForeignKey(
        TodoList,
        related_name="items",
        on_delete=models.CASCADE,
    )
    notes = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    # Order by completed first, then due_date, then created_on
    class Meta:
        ordering = [
            "completed",
            "due_date",
            "created_on",
        ]
