from django.shortcuts import render, HttpResponseRedirect
from .models import Empleados
from django.forms import modelform_factory

def index(request):

    cantidad_empleados = Empleados.objects.count()
    listar_empleados = Empleados.objects.all() #para obtener todos los registros
    return render(request, 'index.html', {'cantidad_empleados':cantidad_empleados, 'listar_empleados':listar_empleados})





def detalleEmpleados(request, id):
    empleado = Empleados.objects.get(pk=id)
    return render(request, 'detalle_emp.html', {'empleado': empleado})



FormEmpleado = modelform_factory(Empleados, exclude=[])

def formEmpleado(request):
    if request.method == 'POST':
        formEmpleado = FormEmpleado(request.POST)
        if formEmpleado.is_valid():
            formEmpleado.save()
            
        else:
           return render(request, 'nuevo_emp.html', {'formEmpleado': formEmpleado}) 
    else: 
        formEmpleado = FormEmpleado()
        return render(request, 'nuevo_emp.html', {'formEmpleado': formEmpleado})
    
