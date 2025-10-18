from django import forms
from django.core.exceptions import ValidationError
from .models import ContactUs

# class ContactUsForms(forms.Form):
#     birth_year = forms.DateField(widget=forms.SelectDateWidget)
#     name = forms.CharField(max_length=300, label='your name')
#     email = forms.EmailField(max_length=100, label='your email')
#     subject = forms.CharField(max_length=10, label='your subject')
#     description = forms.Textarea()
    
#     def clean(self):
#         name = self.cleaned_data.get('name')
#         subject = self.cleaned_data.get('subject')
        
#         if name == subject:
#             raise ValidationError('name and subject are same')
        
#     def clean_name(self):
#         name = self.cleaned_data.get('name')
        
#         if 'n' in name:
#             raise ValidationError('n is not good for your name!')
        
#         return name

# model form
class ContactUsForms(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'})
        }