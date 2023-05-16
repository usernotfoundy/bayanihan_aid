from django import forms
from myapp.models import Applicant

class ApplicantForm(forms.ModelForm):
    
    class Meta:
        model = Applicant
        fields = ['name', 'address', 'income', 'gender', 'appdate', 'apptime','status']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'income': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-check'},
                                    choices=Applicant.GENDER_CHOICES),
            'appdate': forms.TextInput(attrs={'class': 'form-control'}),
            'apptime': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select appointment time'},
                                    choices=Applicant.TIME_CHOICES),
            'status': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
        }
