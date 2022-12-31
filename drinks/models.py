from django.db import models

class drink(models.Model):
    name = models.CharField(max_length=500)
    descripton = models.CharField(max_length=200)

    def __str__(self):
        return self.name + '' + self.descripton