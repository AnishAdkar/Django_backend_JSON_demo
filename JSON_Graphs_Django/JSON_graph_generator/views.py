from django.shortcuts import render

def fun1(request):
    return render(request, "home_json.html")
