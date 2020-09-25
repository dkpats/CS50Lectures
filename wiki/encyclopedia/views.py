from django.shortcuts import render
from markdown2 import Markdown
from random import randint
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

def search(request):
    
    #store the client's search
    search = request.GET['q']

    # if the search string is a page, load that page
    # but this seems to be causing only upper case to match
    """
    if search in util.list_entries():
        return entry(request, search)
    """
    #trying this to avoid the issue with upper case
    substrings = []
    resultCount = 0

    for pages in util.list_entries():
        # if query matches name of an encyclopedia entry, display that entry
        if search.lower() == pages.lower():
            return entry(request, search)
        elif search.lower() and pages.lower().find(search.lower()) >= 0:
            substrings.append(pages.lower())

    if len(substrings):
        resultCount = len(substrings)
            
        # if the query does not match the name of an encyclopedia entry, the user should
        # instead be taken to a search results page that displays a list of all encyclopedia
        # entries that have the query as a substring. For example, if the search query were
        # Py, then Python should appear in the search results.
    
    #if not pages match even the substring, show "0 results found"
    #else:
    title = f"Resuts for \"{search}\""
    return render(request,"encyclopedia/search.html", {
    "title": title,
    "substrings": substrings,
    "resultCount": resultCount
    })

    """
    try:
        present the page the client is looking for
    except TypeError: #  this is what was thrown when I tried using an incorrect URL
        show them an error page tailored to their error
    """
def randomEntry(request):

    entryCount = len(util.list_entries())
    randomPage = util.list_entries()[randint(0,entryCount-1)]
    return entry(request, randomPage)