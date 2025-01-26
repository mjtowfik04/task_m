from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admin_dashboard(request):
    return render(request,"deshboard/manager-deshboard.html")

def user_dashboard(request):
    return render(request,"deshboard/user-dashboard.html")

def test(request):
    return render(request,'test.html')