from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todoTable

# Create your views here.
def home(request):
    todo_data = todoTable.objects.all()
    return render(request, 'index.html',{ 'todo_data': todo_data})

def add(request):
    #get todoitem name from form
    todo_item = request.POST['todo_item']
    #create a new object
    new_todo = todoTable(content = todo_item)
    #save it
    new_todo.save()
    #redirect
    return redirect(home)

def deleteItem(request, todo_id):
    #get todoitem id from form
    item =todoTable.objects.get(id=todo_id)
    item.delete()
    return redirect(home)
