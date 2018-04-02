from django.db import models

class Theme(models.Model):
    """docstring for Theme."""

    title = models.CharField(max_length = 100)
    #slug = models.SlugField()
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "Theme: "+str(self.id)+": "+self.title

    def snippet(self):
        return self.description[:50] + '...'
