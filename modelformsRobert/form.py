from django import forms
from modelformsRobert.model import Register


class MyModel(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['Gender']


class Name(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        widgets = {'Firstname': forms.TextInput(attrs={'placeholder': 'Enter your firstname'}),
                   'Lastname': forms.TextInput(attrs={'placeholder': 'Enter your lastname'})
                   }
