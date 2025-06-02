from django.shortcuts import render
from django.http import HttpResponse


listOfprogramming=['Hello World program','swapping of number','reverse of Number']
def dataTransfer(request):
  if(request.GET.get('userName')!=None):
    listOfprogramming.append(request.GET.get('userName'))
  value = request.GET.get('data', '')
  print(value)
  if request.GET.get('removeData') is not None:
    try: 
      listOfprogramming.pop(int(request.GET.get('removeData')))
    except BaseException as e:
      print(e)
  dict={
    'name':'zafar imam',
    'address':'pune',
    'listOfprogramming':listOfprogramming,
    'value':value,
  }


  return render(request,'fileRander.html',dict)

