from django.shortcuts import render, redirect
from django.http import HttpResponse

from Apps.Aplicacion1.forms import Aplicacion1Form
from Apps.Aplicacion1.models import Actividades
# Create your views here.

def index(request):
    return render(request, 'Aplicacion1/index.html')

def Aplicacion1_view(request):
    if request.method=='POST':
        form=Aplicacion1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aplicacion1_listar')
    else:
        form=Aplicacion1Form()
    return render(request,'Aplicacion1/Aplicacion1_form.html',{'form':form})

def Aplicacion1_list(request):
    Aplicacion1=Actividades.objects.all().order_by('id')
    return render(request,'Aplicacion1/Aplicacion1_list.html', {'Aplicaciones':Aplicacion1})

def Aplicacion1_edit(request, id_Aplicacion1):
    Aplicacion1=Actividades.objects.get(id=id_Aplicacion1)
    if request.method=='GET':
        form=Aplicacion1Form(instance=Aplicacion1)
    else:
        form=Aplicacion1Form(request.POST,instance=Aplicacion1)
        if form.is_valid():
            form.save()
        return redirect('Aplicacion1_listar')
    return render(request,'Aplicacion1/Aplicacion1_form.html',{'form':form})

def Aplicacion1_delete(request, id_Aplicacion1):
    Aplicacion1=Actividades.objects.get(id=id_Aplicacion1)
    if request.method=='POST':
        Aplicacion1.delete()
        return redirect('Aplicacion1_listar')
    return render(request,'Aplicacion1/Aplicacion1_delete.html',{'Aplicacion1':Aplicacion1})