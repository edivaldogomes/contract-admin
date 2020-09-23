from django.urls import path
from .views import *
from .report import *

# Create your views here.
app_name = "pedido"
urlpatterns = [
	# URLS OF PROVINCE
	path('listar/provincia',ProvinciaList.as_view(),name='listar_provincia'),
	path('eliminar/provincia/<int:pk>',ProvinciaDelete.as_view(),name='delete_provincia'),
	path('modificar/provincia/<int:pk>',ProvinciaUpdate.as_view(),name='update_provincia'),
	path('criar/provincia',ProvinciaCreate.as_view(),name='create_provincia'),

	# URLS OF CITY
	path('listar/municipio',MunicipioList.as_view(),name='listar_municipio'),
	path('eliminar/municipio/<int:pk>',MunicipioDelete.as_view(),name='delete_municipio'),
	path('modificar/municipio/<int:pk>',MunicipioUpdate.as_view(),name='update_municipio'),
	path('criar/municipio',MunicipioCreate.as_view(),name='create_municipio'),

	# URLS OF COMMUNE
	path('listar/comuna',ComunaList.as_view(),name='listar_comuna'),
	path('eliminar/comuna/<int:pk>',ComunaDelete.as_view(),name='delete_comuna'),
	path('modificar/comuna/<int:pk>',ComunaUpdate.as_view(),name='update_comuna'),
	path('criar/comuna',ComunaCreate.as_view(),name='create_comuna'),

	# URLS OF SPACE LEGALIZER
	path('criar/terreno/legalizar',CreateLegalizarView.as_view(),name='create_legalizar'),
	path('modificar/terreno/<int:pk>/',UpdateLegalizarView.as_view(),name='update_legalizar'),
	path('listar/terrenos/',ListLegalizarView.as_view(),name='listar_legalizar'),
	path('detalhe/terreno/<int:pk>',DetailLegalizarView.as_view(),name='detail_legalizar'),
	path('eliminar/terreno/<int:pk>',DeleteLegalizarView.as_view(),name='delete_legalizar'),
	path('ver_pdf/<int:pk>', pdf, name='pdf'),

	# URLS OF SPACE FINISH LEGALIZER
	path('criar/pagos/<int:pk>/',CreateTerminadoView,name = 'create_terminado'),
	path('listar/processos/terminados',ListTerminadoView.as_view(),name = 'listar_terminado'),
	path('modificar/processos/<int:pk>/terminado',UpdateTerminadoView.as_view(),name='update_terminado'),
	path('detalhe/processo/<int:pk>',DetailTerminadoView.as_view(),name='detail_terminado'),

	# URLS OF PDF
	path('gerar/pdf/<int:pk>',GenerarPDF.as_view(),name='gerar_pdf'),

	# URLS OF DIRECTER
	path('listar/directivo/',ListDirectivoView.as_view(),name = 'listar_directivo'),
	path('criar/directivo/',CreateDirectivoView.as_view(),name = 'create_directivo'),
	path('modificar/directivo/<int:pk>/',UpdateDirectivoView.as_view(),name = 'update_directivo'),
	path('eliminar/directivo/<int:pk>/',DeleteDirectivoView.as_view(),name = 'delete_directivo'),
]
