from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True, help_text='Introduce un correo electronico valido')

    class Meta():
        model = User
        fields = ['first_name' , 'last_name' , 'username' ,  'email' , 'password1' , 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado.")
        return email


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







# class UserForm(forms.ModelForm):
#     class Meta():
#         model = User
#         fields = ['first_name' , 'last_name' ,'username' , 'email' , 'password' ]