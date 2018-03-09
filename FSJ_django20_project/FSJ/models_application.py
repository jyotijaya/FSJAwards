import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from .models_award import Award
from .models_FSJUser import FSJUser

class Application(models.Model):
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name='applications')
    student = models.ForeignKey(FSJUser, on_delete=models.CASCADE, related_name='applications', to_field='ccid')
    is_submitted = models.BooleanField(verbose_name = _("Is Submitted"))
    
    def __str__(self):
        return self.student.ccid + "'s application for " + self.award.award_name    
    
    def getawardname(self):
        return self.award.award_name
    
    def getstudentccid(self):
        return self.student.ccid