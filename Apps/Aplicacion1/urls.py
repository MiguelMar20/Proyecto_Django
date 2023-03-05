from django.urls import include, path
from Apps.Aplicacion1.views import index, Aplicacion1_view, Aplicacion1_list, Aplicacion1_edit, Aplicacion1_delete

urlpatterns = [
    path('index/', index, name="index"),
    path('nuevo/', Aplicacion1_view, name="Aplicacion1_crear"),
    path('lista/', Aplicacion1_list, name="Aplicacion1_listar"),
    path('edita/<int:id_Aplicacion1>/', Aplicacion1_edit, name="Aplicacion1_editar"),
    path('elimina/<int:id_Aplicacion1>/', Aplicacion1_delete, name="Aplicacion1_eliminar"),
]