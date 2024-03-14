from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def retrieve_page(request,name):
    return HttpResponse("util.get_entry(name)")

