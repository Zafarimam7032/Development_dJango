from django.http import HttpResponse

def viewPage(request):
  print("this is first view first project")
  return HttpResponse("<h1>this is view page</h1>")