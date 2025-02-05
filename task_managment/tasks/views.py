from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task,TaskDetail
# Create your views here.
def admin_dashboard(request):
    return render(request,"deshboard/manager-deshboard.html")

def user_dashboard(request):
    return render(request,"deshboard/user-dashboard.html")

def test(request):
    return render(request,'test.html')

def create_text(request):
    # employee= Employee.objects.all()
    form= TaskModelForm() #For Get

    if(request.method =="POST"):
        form=TaskModelForm(request.POST)
        if(form.is_valid()):
            # form data
            form.save()

            return render(request,"task_from.html",{"form":form,"message":"task added successfull"})
  
    context={"form":form}
    return render(request,"task_from.html",context)

def view_task(request):

    # tasks=Task.objects.filter(status="PENDING")
    # tasks=TaskDetail.objects.exclude( priority="H")
    tasks=Task.objects.all()
    return render(request,"show_task.html",{"tasks":tasks})

 