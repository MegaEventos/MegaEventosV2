from django.shortcuts import render
from clients.models import Clients
from office.models import Paquetes
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy

from clients.forms import ClientsForm

# PDF

import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    clients = Clients.objects.all()
    paquetes = Paquetes.objects.all()
    # clients = Clients.objects.filter()
    return render(request, 'index.html', {'clients':clients, 'paquetes':paquetes})


@login_required(login_url='/accounts/login/')
def edit(request, clave_id):
    # Recuperamos la instancia de la persona
    instancia = Clients.objects.get(id=clave_id)

    # Creamos el formulario con los datos de la instancia
    form = ClientsForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # print('Printing post', request.POST)
        # Actualizamos el formulario con los datos recibidos
        form = ClientsForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

        return redirect('home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "edit.html", {'form': form, 'instancia':instancia})


@login_required(login_url='/accounts/login/')
def delete(request, clave_id):
    instancia = Clients.objects.get(id=clave_id)
    instancia.Recycle = True
    instancia.save()
    
    return redirect('home')


@login_required(login_url='/accounts/login/')
def restore(request, clave_id):
    instancia = Clients.objects.get(id=clave_id)
    instancia.Recycle = False
    instancia.save()
    
    return redirect('reciclaje')


@login_required(login_url='/accounts/login/')
def reciclaje(request):
    clients = Clients.objects.all()
    return render(request, 'recycle.html', {'clients':clients})










# def portfolio(request):

#     form = PortfolioForm()
#     if request.method == 'POST':
#         #print('Printing post', request.POST)
#         form = PortfolioForm(request.POST)

#         if form.is_valid():
#             instace = form.save(commit=False)
#             instace.user = request.user
#             instace.save()
#             #form.save()


#             portfolio_info = {
#                 'portfolio_name':instace.portfolio_name
#             }
            
#             print(portfolio_info['portfolio_name'])

#             return redirect('transactions')

#     context = {'form' : form}

#     return render(request, 'backapp/portfolio.html', context)




# def transactions(request):

#     form = TransactionForm()
#     if request.method == 'POST':
#         #print('Printing post', request.POST)
#         form = TransactionForm(request.POST)

#         if form.is_valid():
#             instace = form.save(commit=False)
#             instace.save()

#             return redirect('../')

#     context = {
#         'form' : form
#     }
#     return render(request, 'backapp/transaction.html', context)














# def Office(request):
#     profile = Profile.objects.filter(referenceID=request.user.profile.id)
#     socio = Profile.objects.filter(id=request.user.profile.referenceID)
#     level = Level.objects.all()
#     return render(request,'office/office.html', {'profile':profile,'socio':socio, 'level':level})




def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('pdf.html')
            context = {
                'clients': Clients.objects.get(pk=self.kwargs['pk']),
                'paquetes': Paquetes.objects.all()
            }
            html = template.render(context)

            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"' #Esta funcion descarga automaticamente los PDF

            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response, link_callback=link_callback)
            # if error then show some funy view
            # if pisa_status.err:
            #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response

        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))