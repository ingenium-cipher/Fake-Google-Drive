from django.db import models


class File(models.Model):

    description = models.TextField()
    files = models.FileField(upload_to='')

    def __str__(self):
        return self.description
# Create your models here.
