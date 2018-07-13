from django.urls import path
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate

app_name = 'mascota'
urlpatterns = [
    path('', index, name='index'),
    path('nuevo', MascotaCreate.as_view(), name='mascota_crear'),
    # path('nuevo', mascota_view, name='mascota_crear'),
    path('listar', MascotaList.as_view(), name='mascota_listar'),
    # path('listar', mascota_list, name='mascota_listar'),
    path('edit/<mascota_id>/', mascota_edit, name='mascota_editar'),
    path('eliminar/<mascota_id>/', mascota_delete, name='mascota_eliminar'),

]
