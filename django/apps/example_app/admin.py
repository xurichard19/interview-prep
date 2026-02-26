from django.contrib import admin

from .models import ExampleModel

admin.site.register(ExampleModel) # if we want access to the model in the admin panel, we have to register it here