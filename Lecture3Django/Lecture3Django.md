# Lecture 3 - Django

I'll be making an effort in this set of notes to write in Markdown, a widely accepted file format that translates a few conventions into HTML for portable viewing.

Notes will follow the folling format:

### [TIMESTAMP]
- Example of a bulleted note.
- Example of *another* bulleted note.
-   One **final** example of a bulletd note, with code:
    > `coding = example[2]`


### [0:00 - Introduction][1]
- We will use Django to make *dynamic* web pages
- Our goal: Write software that will run on a web server so clients (in their browser) can make requests to our server, and receive a response from our server
-   we will use HTTP (hyper text transfer protocol) to communicated between the server and client (requests & responses)
    1. client makes request
    2. server processes request
    3. server reutrns a response
### [2:40 - HTTP][2]
-   `get` is an example of a request method

    get ***request*** example:
    >`get / HTTP/1.1`
    >
    >`Host: www.example.com`
    >
    >`...`
    
    - this might be read as:
        > *I'm a client that would like to get "/", the root of the website. I'm communicating using HTTP version 1.1, and I'm requesting this from the host www.example.com.*

    get ***response*** example:
    >`HTTP/1.1 200 OK`
    >
    >`Content-type: text/html`
    >
    >`...`
    
    This might be read as:
    
    > *The server processed your request used HTTP version 1.1, and your response code is 200, or, "OK". The information here is text/html, so render it accordingly.*

- the key is to think about the web in terms of requests and responses

### [4:59 - Django][3]
- Django is a prebuilt web framwork that takes a lot of the nitty gritty work out and allows us to write python code to quickly build web applications
-   to start a Dajango project, run the following command:
    >`django-admin  startproject <projectname>`
    
    This sets up a number of starter files for you by default.

- `manage.py` is a file we'll use to interact with the project, but not a file we're going to make a lot (or any) changes to
- `urls.py` is a table of contents for all the URLs on my application
- `python manage.py <command>` will be how we use `manage.py`. We can use the `runserver` command to launch our project.
- Django projects consist of one or more Django applications. Think Google, with images, maps, etc.
- `Ctrl + C` will exit a Django app running (at least the default in development mode) 
- we can start a Django Application by running `'manage.py' startapp <appname>`
- You then need to install this app by configuring settings.py, by adding the `<appname>` to `INSTALLED_APPS`
- each view will be something a user might want to see
- once you create a view for the applicaion, you'll need to let it know what URL to visit to get that view. For this, we'll create a new file in the hello directory that contains our URLs
- then, you need to tell the project what apps to include and the URLs to access them, by updating the `urls.py` file in the project folder

[1]: https://youtu.be/w8q0C-C1js4?t=0
[2]: https://youtu.be/w8q0C-C1js4?t=160
[3]: https://youtu.be/w8q0C-C1js4?t=299