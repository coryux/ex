from django.shortcuts import render

def epics(request):
    return render(request,'epics/epics.html')

def epic(request, number):
    return render(request,'epics/epics.html',{'number':number})
