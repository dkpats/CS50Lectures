from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "todolist" not in request.session:
        request.session["todolist"] = []
    return render(request, "todolist/index.html", {
        "todolist": request.session["todolist"]
    })

def addtask(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["todolist"] += [task]
            return HttpResponseRedirect(reverse("todolist:index"))
        else:
            return render(request, "todolist/addtask.html", {
                "form": form
            })
    
    return render(request, "todolist/addtask.html", {
        "form":NewTaskForm()
    })