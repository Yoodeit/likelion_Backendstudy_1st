from django import forms
from .models import Model1forUpload, Model1forComment

class uploadform1(forms.ModelForm):
    class Meta:
        model = Model1forUpload
        fields = '__all__'

class commentuploadform1(forms.ModelForm):
    class Meta:
        model = Model1forComment
        fields = '__all__'