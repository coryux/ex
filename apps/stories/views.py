from django.shortcuts import render

def stories(request):
    return render(request,'stories/stories.html')

def story(request, number):
    return render(request,'stories/stories.html',{'number':number})
