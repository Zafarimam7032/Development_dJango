from django.http import HttpResponse

from django.shortcuts import render

def viewPage(request):
  print("this is first view first project")
  # return HttpResponse("<h1>this is view page</h1>")
  return render(request,"Home.html",{})