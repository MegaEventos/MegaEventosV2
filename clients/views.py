from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClientsForm

# Create your views here.

# def index(request):
#     return render(request, 'registroServicio.html')

def error404(request):
    return render(request, 'error-404.html')

def index(request):
    # create object of form
    form = ClientsForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context ={'form':form}
  
    return render(request, "registroServicio.html", context)

# def clients_view(request):
#     # create object of form
#     form = ClientsForm(request.POST or None, request.FILES or None)

#     context ={'form':form}
      
#     # # check if form data is valid
#     # if form.is_valid():
#     #     # save the form data to model
#     #     form.save()
  
#     return render(request, "registroServicio.html", context)





# class SignUpView(CreateView):
#     form_class = UserCreationFormWithEmail
#     template_name = 'registration/register.html'

#     def get_success_url(self):
#         return reverse_lazy('login') + '?register'

#     def get_form(self, form_class=None):
#         form = super(SignUpView, self).get_form()

#         form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombres'})
#         form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellidos'})
#         form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
#         form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo electronico'})
#         form.fields['referenceID'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'ID Referido'})
#         form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
#         form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
#         return form