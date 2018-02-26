from .models_award import Award
from django.forms import ModelForm, CheckboxSelectMultiple

#Modelform for an award, this restricts what fields will be enabled/disabled as well as widgets, etc
class AwardForm(ModelForm):

    class Meta:
        model = Award
        exclude = ()
        fields = ('award_name', 'description', 'value', 'programs', 'years_of_study', 'deadline', 'documents_needed', 'is_active')

    def __init__(self, *args, **kwargs):
        super(AwardForm, self).__init__(*args, **kwargs)
        
        
    