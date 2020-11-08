from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title
