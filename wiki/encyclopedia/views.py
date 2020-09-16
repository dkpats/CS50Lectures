from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner = Markdown()
    htmlEntry = markdowner.convert(util.get_entry(entry))
    return render(request, "encyclopedia/entry.html", {
        "title": entry.capitalize(),
        "entry": htmlEntry
    })