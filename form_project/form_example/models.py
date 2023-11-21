from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=4)
    number = models.CharField(max_length=4)
    description = models.CharField(max_length=255)

    # this is a built-in method that returns a string representation of an object
    def __str__(self) -> str:
        return f"{self.prefix} {self.number}: {self.name}"
