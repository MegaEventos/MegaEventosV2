# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import Clients
  
# create a ModelForm
class ClientsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Clients
        fields = "__all__"

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['avatar', 'bio', 'link', 'phone']
#         widgets = {
#             'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
#             'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
#             'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
#             'phone': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Telefono'}),
#         }