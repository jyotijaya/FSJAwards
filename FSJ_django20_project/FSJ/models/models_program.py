from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid


class Program(models.Model):
    """Represents a university program which students can join

    id -- autogenerated unique ID
    code -- the short generally 5-character code representing the program
    name -- the full name of the program
    """

    class Meta():
        ordering = ('name',)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length = 10, unique=True, verbose_name = _("Program Code"))
    name = models.CharField(max_length = 255, verbose_name = _("Program Name"))
    
    def __str__(self):
        return self.name