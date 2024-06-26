# Generated by Django 5.0.6 on 2024-05-31 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="TodoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task", models.CharField(max_length=255)),
                ("notes", models.TextField(blank=True, null=True)),
                ("completed", models.BooleanField(default=False)),
                ("due_date", models.DateTimeField(blank=True, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "todolist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="todos.todolist",
                    ),
                ),
            ],
            options={
                "ordering": ["completed", "due_date", "created_on"],
            },
        ),
    ]
