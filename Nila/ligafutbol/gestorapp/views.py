from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from gestorapp.models import Liga
from gestorapp.forms import Gestorappform

#agregar
def NuevaPersona(request):
    if request.method=="POST":
        FormaPersona = Gestorappform(request.POST)
        if FormaPersona.is_valid():
            FormaPersona.save()
            return redirect("listadoPersonas")
    else:
        FormaPersona = Gestorappform()
    return render(request, "nuevo.html",{'formaPersona': FormaPersona})
#editar
def editarPersona(request,id):
    persona = get_object_or_404(Gestorapp,pk=id)
    if request.method =='POST':
        formaPersona = Gestorappform(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect("listadoPersonas")
    else:
        formaPersona = Gestorappform(instance=persona)
        return render(request,"editarPersona.html",{"formaPersona": formaPersona})

def eliminarPersona(request,id):
    persona = get_object_or_404(Gestorapp,pk=id)
    if persona:
        persona.delete()
    return redirect("listadoPersonas")


def detallePersona(request, id):
    persona = get_object_or_404(Gestorapp,pk=id)
    return render(request, "detallePersona.html", {"persona": persona})