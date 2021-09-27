from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import ToDo

# Create your views here.

@login_required
def index(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        if 'todo' in request.POST:
            todo_to_add = request.POST['todo']
            todo = ToDo.objects.create(user=user, title=todo_to_add)
            todo.save()
        else:
            if 'del-single' in request.POST:
                todo_id_to_del = request.POST['del-single']
                todo = ToDo.objects.get(id=todo_id_to_del)
                todo.delete()
            elif 'delete_all' in request.POST:
                todos = ToDo.objects.all()
                print(todos)
                todos.delete()
            print(request.POST)

    todo = ToDo.objects.filter(user=user)
    context = {
        'todoes': todo,
        "numbers_of_todo": len(todo)
    }
    return render(request, "index.html", context)

