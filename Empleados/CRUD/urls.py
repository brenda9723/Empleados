from django.urls import path
from . import views


urlpatterns={
    path('', views.index, name="index"), #importa la funcion index que se define en el modulo views
    path('detalle_empleados/<int:id>', views.detalleEmpleados, name="detalle_emp"),  #definis el path a donde se va ir a buscar seguido del valor de la llave primaria para verle
    #esa barra int:id seria la forma en la que le vas a obtener a tu objeto, en este caso en la funcion se pone que el get se hace por id
    path('nuevo_empleado', views.formEmpleado, name='nuevo_emp')
}

