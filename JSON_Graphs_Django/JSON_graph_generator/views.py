from django.shortcuts import render

def fun1(request):
    return render(request, "home_json.html")

def fun2(request):
    return render(request, "graph.html")

def fun3(request):
    return render(request, "exit.html")
