from django.shortcuts import render, redirect
from markdown2 import Markdown
from random import randint
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):

    markdowner = Markdown()
    try:
        htmlEntry = markdowner.convert(util.get_entry(entry))
    except TypeError:
        return errorPage(request, "404: Page not found.")

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

    title = f"Resuts for \"{search}\""
    return render(request,"encyclopedia/search.html", {
    "title": title,
    "substrings": substrings,
    "resultCount": resultCount
    })

def randomEntry(request):

    entryCount = len(util.list_entries())
    randomPage = util.list_entries()[randint(0,entryCount-1)]
    return redirect(entry, randomPage)

def newEntry(request):

    return render(request, "encyclopedia/newEntry.html")

def saveNewEntry(request):

    title = request.GET['Title']

    if title in util.list_entries():
        return errorPage(request, "An entry with that title already exists.")
    else:
        content = request.GET['Entry Content']
        util.save_entry(title, content)
        return redirect(entry, title)

def editEntryPage(request):
    
    return render(request, "encyclopedia/editEntryPage.html",{
        "title": request.GET['entry'],
        "entryContent": util.get_entry(request.GET['entry'])
    })

def saveEntryEdits(request):
    print(request.GET)
    title = request.GET['Title']
    content = request.GET['Entry Content']
    util.save_entry(title, content)
    return redirect(entry, title)

def errorPage(request, message):
    return render(request, "encyclopedia/errorPage.html", {
        "message": message
    })