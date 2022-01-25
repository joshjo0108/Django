from django.db import models
from sorl.thumbnail import ImageField


# THE THINGS YOU NEED IN Post CLASS
# TEXT
# IMAGE
class Post(models.Model):
    # IT TAKES A CHARACTER LENGTH OF 140 AND IT SHOULDN'T BE NULL NOR BLANK
    text = models.CharField(max_length=140, blank=False, null=False)
    # UPLOAD ANY FORM OF IMAGE
    image = ImageField()


    # THIS WILL UPDATE POST TITLE
    def __str__(self):
        return self.text
