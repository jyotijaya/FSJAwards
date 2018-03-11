from .models_coordinator import Coordinator
from django.forms import ModelForm

class CoordinatorForm(ModelForm):

    class Meta:
        model = Coordinator
        fields = ('ccid', 'first_name', 'last_name', 'email', 'lang_pref', 'ualberta_id')
        
    def __init__(self, *args, **kwargs):
        super(CoordinatorForm, self).__init__(*args, **kwargs)               
        
    
class CoordinatorRestrictedForm(ModelForm):

    class Meta:
        model = Coordinator
        fields = ('ccid', 'first_name', 'last_name', 'email', 'lang_pref', 'ualberta_id')
        
    def __init__(self, *args, **kwargs):
        super(CoordinatorRestrictedForm, self).__init__(*args, **kwargs)
        self.fields['ccid'].disabled=True
        self.fields['email'].disabled=True