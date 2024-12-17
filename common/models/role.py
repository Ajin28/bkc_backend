from django.db import models
from django.utils.translation import gettext_lazy as _




# Role Model
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name