from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


@login_required
def todo_list_list(request: HttpRequest) -> HttpResponse:
    todos = TodoList.objects.filter(user=request.user)
    return render(request, "todos/list.html", {"todo_list_list": todos})


@login_required
def show_list(request: HttpRequest, id: int) -> HttpResponse:
    todolist = get_object_or_404(TodoList, id=id, user=request.user)
    return render(request, "todos/detail.html", {"todolist": todolist})


@login_required
def create_list(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = form.save(commit=False)
            todolist.user = request.user
            todolist.save()
            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoListForm()
    return render(request, "todos/create.html", {"form": form})


@login_required
def create_item(request: HttpRequest, list_id=None) -> HttpResponse:
    todolist = get_object_or_404(TodoList, id=list_id, user=request.user)
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todoitem = form.save(commit=False)
            todoitem.user = request.user
            todoitem.todolist = todolist
            todoitem.save()
            return redirect("todo_list_detail", id=todoitem.todolist.id)
    else:
        initial_data = {"todolist": todolist}
        form = TodoItemForm(initial=initial_data)
    return render(request, "todos/create_item.html", {"form": form, "list_id": list_id})


@login_required
def edit_list(request: HttpRequest, id: int) -> HttpResponse:
    todolist = get_object_or_404(TodoList, id=id, user=request.user)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todolist)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todolist)
    return render(
        request,
        "todos/edit.html",
        {
            "form": form,
            "todolist": todolist,
        },
    )


@login_required
def edit_item(request: HttpRequest, id: int) -> HttpResponse:
    todoitem = get_object_or_404(TodoItem, id=id, user=request.user)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todoitem)
        if form.is_valid():
            updated_item = form.save()
            return redirect("todo_list_detail", id=updated_item.todolist.id)
    else:
        form = TodoItemForm(instance=todoitem)
    return render(
        request,
        "todos/edit_item.html",
        {
            "form": form,
            "todoitem": todoitem,
        },
    )


@login_required
def delete_list(request: HttpRequest, id: int) -> HttpResponse:
    todolist = get_object_or_404(TodoList, id=id, user=request.user)
    if request.method == "POST":
        todolist.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html", {"id": id})


@login_required
def search(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")
    if query:
        results = TodoItem.objects.filter(
            Q(task__icontains=query) | Q(notes__icontains=query),
            user=request.user,
        )
    else:
        results = TodoItem.objects.none()
    return render(
        request,
        "todos/search_results.html",
        {"results": results, "query": query},
    )


@login_required
def delete_item(request: HttpRequest, id: int) -> HttpResponse:
    todoitem = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        todolist_id = todoitem.todolist.id
        todoitem.delete()
        return redirect("todo_list_detail", id=todolist_id)
    return render(request, "todos/delete_item.html", {"todoitem": todoitem})
