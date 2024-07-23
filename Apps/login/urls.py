from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registro.html', views.registro_view, name='registro'),
    path('login.html', views.login_view, name='login'),
    path('sistema.html', views.sistema_view, name='sistema'),
    path('registro/', views.RegistroUsuario, name='registrar_usuario'),  
    path('login/', views.iniciar_sesion, name='login'),
    path('ordenCompleta.html',views.ordenCompleta_view, name='ordenCompleta'),
    path('base.html',views.base_view, name='base'),
    path('extends.html',views.extends_view, name='extends'),
    path('empleado.html',views.empleado_view, name='empleado'),
    path('gerente.html',views.gerente_view, name='gerente'),
    path('proveedores.html',views.proveedores_view, name='proveedores'),    
    path('edicionProveedores.html', views.edicionProveedores_view, name='edicionProveedores' ),
    path('gestionProveedores.html', views.gestionProveedores_view, name='gestionProveedores'),  
    path('registrarProveedores/', views.registrarProveedores),
    path('edicionProveedores/<codigo>', views.edicionProveedores),
    path('editarProveedores/', views.editarProveedores),
    path('eliminarProveedores/<codigo>', views.eliminarProveedores),
    path('RegistroProveedores/', views.RegistroProveedores)
]