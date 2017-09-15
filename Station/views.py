from django.shortcuts import render

from Station.models import Reading

def home(request):
    data = Reading.objects.last()
    return render(request,'home.html',{'data':data})
