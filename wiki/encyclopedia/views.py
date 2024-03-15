from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def retrieve_page(request,name):
    list_of_entries = util.list_entries()
    if name not in list_of_entries:
        return render(request, "encyclopedia/no_entry.html", {
            "name" : name
        })
    else:
        return HttpResponse(util.get_entry(name))


