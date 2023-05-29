from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def projectsUrlFunc(request):
    return HttpResponse("Here are our products url page")


'''
Passing Dynamic Data
'''

def singleProjectPage(request, id):
    return HttpResponse("Here are our Single project products url page: Id is: "+str(id))
