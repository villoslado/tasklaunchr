from django.urls import path
from todos.views import (
    todo_list_list,
    show_list,
    create_list,
    create_item,
    edit_list,
    edit_item,
    delete_list,
)

urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", show_list, name="todo_list_detail"),
    path("create/", create_list, name="todo_list_create"),
    path("items/create/", create_item, name="todo_item_create"),
    path("<int:id>/edit/", edit_list, name="todo_list_update"),
    path("items/<int:id>/edit/", edit_item, name="todo_item_update"),
    path("<int:id>/delete/", delete_list, name="todo_list_delete"),
]
