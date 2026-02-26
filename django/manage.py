# this file runs every time we run our application through py manage.py runserver

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
django basics (didnt know a better place to put this)

model view template design: django applications are divided into three main components...

    - model: layer which defines the structure and logic for storing and manipulating data, models are python classes
    that use python's object relational mapper (convert oop language to sql query) to interact with the database
    (postgresql, mysql, etc.) without writing actual queries, a model represents an entity stored in the db

        ex.
        class <model>(models.Model):
            <field> = models.<field type>(<field characteristics>)
    
    - view: processes user requests and returns responses by collecting data from model objects and perform logic on
    them then pass the data to the template for display

        ex.
        def <view>(request):
            <view logic>
            return render(request, <template>, <context>)

    - template: renders final html output to browser, we combine html and django template language, we can use {% %}
    and {{ }} to access variables defined in views

        ex.
        html...
        <p>{{ <model>.<field> }}</p>
        html...

the full request flow goes something like: http request -> wsgi creates httprequest object -> middleware handles request,
authentication, sessions, etc. -> url routing -> httprequest passes into view function -> view interacts with db through
models -> render html through template -> generated httpresponse travels back up to the wsgi which then passes it to the 
web server and then the client browser

a django project is composed of multiple reuseable apps, with each app having its own models/views/urls/templates/logic/etc.

some other neat django features: admin panel gives gui for managing db, built in session-based auth

when we first create our project, startproject creates our global config for the website and then we use startapp to create
our individual apps (features)
"""