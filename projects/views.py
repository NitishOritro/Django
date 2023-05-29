from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.






def projectsUrlFunc(request):
    msg = "Hello, you are the project page"
    
    number = 10
    
    context = {'message': msg, 'number': number}
    
    #return render(request, 'projects/projects.html', {'message': msg})
    return render(request, 'projects/projects.html', context)


#Passing Dynamic Data

def singleProjectPage(request, id):
    #return HttpResponse("Here are our Single project products url page: Id is: "+str(id))
    return render(request, 'projects/single-project.html')

#URL Based views


'''
def projectsUrlFunc(request):
    return HttpResponse("Here are our products url page")



#Passing Dynamic Data

def singleProjectPage(request, id):
    return HttpResponse("Here are our Single project products url page: Id is: "+str(id))


'''