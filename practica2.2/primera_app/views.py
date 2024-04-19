from django.shortcuts import render
from django.http import HttpResponse
from primera_app.models import Topic, Webpage, AccessRecord, Los_tres_mosqueteros
from . import forms

# Create your views here.
#def index(request):
 #   my_context = {'username':'Dania'}
  #  return render(request, 'primera_app/index.html', context = my_context)
    #return HttpResponse("Clase de Programación Back End")

def index(request):
    access_list = AccessRecord.objects.order_by('date')
    tres_mosqueteros_list = Los_tres_mosqueteros.objects.order_by('email')
    my_context = {'username': 'Hola desde views.py',
                  'access_records': access_list,
                  'mosqueteros':tres_mosqueteros_list}
    return render(request, 'primera_app/index.html', context=my_context)
    #return HttpResponse("<h1>Recuerdo el día en que de la chamba yo me enamoré</h1>")

# Crear un formulario para mostrar
def form_user_view(request):
    form = forms.FormUser()
    return render(request, 'primera_app/form_page.html', {'form':form})