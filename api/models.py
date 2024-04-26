from django.db import models

# Create your models here.
class Issue(models.Model):
    name: models.CharField = models.CharField(max_length=10)

    @property
    def source_name(self):
        pass
