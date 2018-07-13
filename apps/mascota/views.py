from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse

from django.http import HttpResponse
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
# Create your views here.

def index(request):
    return render(request, 'mascota/index.html',{})

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    else:
        form = MascotaForm()
        print(form)
    return render(request, 'mascota/mascota_form.html', {'datos':form, 'edit':False})

def mascota_list(request):
    # mascota = Mascota.objects.all().order_by('id')
    mascota = Mascota.objects.all()
    contexto = {
        'mascota': mascota,
    }
    # print(mascota)
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, mascota_id):
    id_mascota = mascota_id
    masco = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=masco)
    else:
        form = MascotaForm(request.POST, instance=masco)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'datos':form, 'edit':True})

def mascota_delete(request, mascota_id):
    id_mascota = mascota_id
    masco = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota':masco})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    # return reverse('mascota_listar')
