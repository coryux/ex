from django.shortcuts import render

def themes(request):
    return render(request,'themes/themes.html')

def theme(request, number):
    return render(request,'themes/themes.html',{'number':number})
