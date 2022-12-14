from django.forms import ModelForm
from .models import Discussion

class DiscussionForm(ModelForm):
    class Meta: # Provides meta information
        model = Discussion
        fields = ['name','title','thoughts']