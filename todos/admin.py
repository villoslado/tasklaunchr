from django.contrib import admin
from todos.models import TodoList, TodoItem


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "id",
        "created_on",
    ]
    search_fields = ["name"]
    list_filter = ["created_on"]


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = [
        "task",
        "todolist",
        "created_on",
        "due_date",
        "completed",
    ]
    search_fields = ["task", "notes"]
    list_filter = ["completed", "due_date"]
    ordering = ["completed", "due_date", "created_on"]
