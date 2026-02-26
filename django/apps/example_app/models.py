# handle data in db

from django.db import models

# this would represent a real-world entity like a post or comment
class ExampleModel(models.Model): # must inherit from djangos model
    feature_one = models.CharField(max_length=200)
    feature_two = models.TextField()
    feature_three = models.DateField(auto_now_add=True)

    def __str__(self): # we override the default __str__ implementation to return a more useful str representation
        return self.feature_one
    
"""
VERY IMPORTANT: after making changes to our db (like making a new model), we should call
'python manage.py makemigrations' to create a commit of sorts to the db structure then
call 'python manage.py migrate' to push these changes
"""