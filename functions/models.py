from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Function(models.Model):

    title = models.CharField(
        verbose_name=_('function title'),
        max_length=100,
    )

    def __str__(self):
        return self.title
