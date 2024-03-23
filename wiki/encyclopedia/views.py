from django.shortcuts import render
from django.http import HttpResponse
from .models import entry

from . import util

list_of_entries = util.list_entries()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def retrieve_page(request,name):
    list_of_entries = util.list_entries()
    if name not in list_of_entries:
        return render(request, "encyclopedia/not_found.html", {
            "name" : name
        })
    else:
        return HttpResponse(util.get_entry(name))
    
def search(request):
    if request.method == "POST":
        search_term = request.POST.get('search_term', '')
        list_of_entries = util.list_entries()

        if search_term in list_of_entries:
             return HttpResponse(util.get_entry(search_term))
        else:
            return render(request, "encyclopedia/not_found.html", {
                "name": search_term
            })
    if request.method == "GET":
        return HttpResponse("this works")
    

def new(request):
    if request.method == "POST":
        title = request.POST.get('title',' ')
        body = request.POST.get('body',' ')
        util.save_entry(title,body)
        
    return render(request, "encyclopedia/new.html",)


    
    




