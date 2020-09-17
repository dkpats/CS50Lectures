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
    #htmlEntry = htmlEntry[0:len(htmlEntry)]
    return render(request, "encyclopedia/entry.html", {
        "title": entry.capitalize(),
        "entry": htmlEntry
    })
    """
    try:
        present the page the client is looking for
    except TypeError: #  this is what was thrown when I tried using an incorrect URL
        show them an error page tailored to their error
    """
    
