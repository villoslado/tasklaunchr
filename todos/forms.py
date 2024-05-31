from django import forms
from django.forms import ModelForm
from todos.models import TodoList, TodoItem


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name",
            "description",
        ]
        labels = {
            "name": "List Name",
            "description": "Description",
        }
        help_texts = {
            "name": "Enter a name for your to-do list.",
            "description": "Provide a brief description of this to-do list (optional).",
        }


class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "task",
            "todolist",
            "notes",
            "completed",
            "due_date",
        ]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
            "completed": forms.CheckboxInput(),
        }
        labels = {
            "task": "Task",
            "todolist": "List",
            "notes": "Notes",
            "completed": "Completed",
            "due_date": "Due Date",
        }
        help_texts = {
            "task": "Enter the task description.",
            "todolist": "Select the to-do list this task belongs to.",
            "notes": "Add any additional notes for this task (optional).",
            "completed": "Check if the task is completed.",
            "due_date": "Select the due date for this task.",
        }
