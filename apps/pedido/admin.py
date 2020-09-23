from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Comuna)
admin.site.register(PessoaEmpresa)
admin.site.register(Pago)
admin.site.register(Directivo)


class Terreno_LegalizarAdmin(admin.ModelAdmin):
	list_display = ['projecto','localizacao','provincia_arquivacao','quarterao','municipio','comuna', 'pago_apreciado','pessoaEmpresa','user',]
	list_display_links = ['projecto','localizacao','provincia_arquivacao','quarterao','municipio','comuna', 'pago_apreciado','pessoaEmpresa','user',]
	
admin.site.register(TerrenoLegalizar,Terreno_LegalizarAdmin)