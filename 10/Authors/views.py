from django.shortcuts import render

def showmain2(request):
    return render(request, "Authors/main.html")