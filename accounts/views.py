from django.shortcuts import render , redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#from .forms import UserForm

#from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django import forms

from django.forms.models import model_to_dict

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombres'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellidos'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo electronico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form

# @method_decorator(login_required, name='dispatch')
# class ProfileUpdate(UpdateView):
#     form_class = ProfileForm
#     success_url = reverse_lazy('accounts:profile')
#     template_name = 'profile_form.html'

#     def get_object(self):
#         # Recuperar el objeto que se va a editar
#         profile, created = Profile.objects.get_or_create(user=self.request.user)
#         return profile


# def profile(request):
#     profile = Profile.objects.filter(referenceID=request.user.profile.id)
#     #profile = model_to_dict(request.user.profile)
#     return render(request, 'profileusers.html', {'profile':profile})








# def register(request):
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('/products')

#     else:
#         user_form = UserForm()

#     context = {'user_form' : user_form}

#     return render(request , 'registration/register.html' , context)