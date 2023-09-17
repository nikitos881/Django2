from django.shortcuts import render

def showmain3(request):
    return render(request, "Users/main.html")