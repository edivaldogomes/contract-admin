from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,UpdateView,DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from datetime import datetime, date, time, timezone


#---------------------------------------
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import cgi
import html
#---------------------------------------

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
	data = {
		'title':'inicio'
	}
	return render(request,'accounts/home.html',data)

# Provincia
class ProvinciaList(LoginRequiredMixin, ListView):
	model = Provincia
	template_name = 'provincia/list.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Lista de Provincias'
		return context

class ProvinciaDelete(LoginRequiredMixin, DeleteView):
	model = Provincia
	template_name = 'provincia/delete.html'
	success_url = reverse_lazy("pedido:listar_provincia")
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Provincia'
		return context

class ProvinciaCreate(LoginRequiredMixin, CreateView):
	model = Provincia
	template_name = 'provincia/create.html'
	form_class = ProvinciaForm
	success_url = reverse_lazy('pedido:listar_provincia')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Criar Provincia'
		return context

class ProvinciaUpdate(LoginRequiredMixin, UpdateView):
	model = Provincia
	template_name = 'provincia/create.html'
	form_class = ProvinciaForm
	success_url = reverse_lazy('pedido:listar_provincia')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Editar Provincia'
		return context

# Municipio
class MunicipioList(LoginRequiredMixin, ListView):
	model = Municipio
	template_name = 'municipio/list.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Lista de Municipio'
		return context

class MunicipioDelete(LoginRequiredMixin, DeleteView):
	model = Municipio
	template_name = 'municipio/delete.html'
	success_url = reverse_lazy("pedido:listar_municipio")
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Municipio'
		return context

class MunicipioCreate(LoginRequiredMixin, CreateView):
	model = Municipio
	template_name = 'municipio/create.html'
	form_class = MunicipioForm
	success_url = reverse_lazy('pedido:listar_municipio')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Criar Municipio'
		return context

class MunicipioUpdate(LoginRequiredMixin, UpdateView):
	model = Municipio
	template_name = 'municipio/create.html'
	form_class = MunicipioForm
	success_url = reverse_lazy('pedido:listar_municipio')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Editar Municipio'
		return context

# Comuna
class ComunaList(LoginRequiredMixin, ListView):
	model = Comuna
	template_name = 'comuna/list.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Lista Comunas'
		return context

class ComunaDelete(LoginRequiredMixin, DeleteView):
	model = Comuna
	template_name = 'comuna/delete.html'
	success_url = reverse_lazy("pedido:listar_comuna")
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Comuna'
		return context

class ComunaCreate(LoginRequiredMixin, CreateView):
	model = Comuna
	template_name = 'comuna/create.html'
	form_class = ComunaForm
	success_url = reverse_lazy('pedido:listar_comuna')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Criar Comuna'
		return context

class ComunaUpdate(LoginRequiredMixin, UpdateView):
	model = Comuna
	template_name = 'comuna/create.html'
	form_class = ComunaForm
	success_url = reverse_lazy('pedido:listar_comuna')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Editar Comuna'
		return context

# Legalização de Projecto
class CreateLegalizarView(LoginRequiredMixin, CreateView):
    model = TerrenoLegalizar
    template_name = 'legalizar/create.html'
    form_class = TerrenoLegalizarForm
    second_form_class = PessoaEmpresaForm
    success_url = reverse_lazy('pedido:listar_legalizar')

    def get_context_data(self, *args,**kwargs):
        context = super(CreateLegalizarView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        context['title'] = 'Criar Projecto'
        context['title1'] = 'Requerente'
        context['title2'] = 'Projecto a Legalizar'

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            legalizar = form.save(commit=False)
            legalizar.pessoaEmpresa = form2.save()
            legalizar.user = self.request.user
            legalizar.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class UpdateLegalizarView(LoginRequiredMixin, UpdateView):
	model = TerrenoLegalizar
	second_model = PessoaEmpresa
	template_name = 'legalizar/create.html'
	form_class = TerrenoLegalizarForm
	second_form_class = PessoaEmpresaForm
	success_url = reverse_lazy('pedido:listar_legalizar')

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(UpdateLegalizarView, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		legalizar = self.model.objects.get(id=pk)
		pessoa = self.second_model.objects.get(id=legalizar.pessoaEmpresa_id)
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=pessoa)
		context['id'] = pk
		context['title'] = 'Editar Projecto'
		context['title1'] = 'Requerente'
		context['title2'] = 'Projecto a Legalizar'
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_legalizar = kwargs['pk']
		legalizar = self.model.objects.get(id=id_legalizar)
		pessoa = self.second_model.objects.get(id=legalizar.pessoaEmpresa_id)
		form = self.form_class(request.POST,request.FILES, instance=legalizar)
		form2 = self.second_form_class(request.POST,request.FILES, instance=pessoa)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class ListLegalizarView(LoginRequiredMixin, ListView):
	model = TerrenoLegalizar
	template_name = 'legalizar/list.html'
	def get_context_data(self,*args, **kwargs):
         context = super().get_context_data(**kwargs)
         context['title'] = 'Listado de Projectos em Legalização'
         return context

class DetailLegalizarView(LoginRequiredMixin, DetailView):
    model = TerrenoLegalizar
    template_name = 'legalizar/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalhe do Projecto'
        return context

class DeleteLegalizarView(LoginRequiredMixin, DeleteView):
	model = TerrenoLegalizar
	template_name = 'legalizar/delete.html'
	success_url = reverse_lazy("pedido:listar_legalizar")

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Projecto em Legalização'
		return context

# Projecto Terminado
def CreateTerminadoView(request, pk):
    try:
        terreno_leg = get_object_or_404(TerrenoLegalizar, pk=pk)
        if request.method == 'POST':
            primeiro = request.POST['primeiro']
            segundo = request.POST['segundo']
            terceiro = request.POST['terceiro']
            form = PagoForm(request.POST, request.FILES)
            if form.is_valid():
                Pago.objects.create(
					projecto_legalizado=terreno_leg, primeiro=primeiro, segundo=segundo,
					terceiro=terceiro,
				)
            return redirect('pedido:listar_terminado')
        else:
            form = PagoForm()
            data = {
		        'form': form,
			    'title':'Adicionar o Pago'
            }
        return render(request, 'terminado/create.html',data)
    except Exception as e:
        messages.warning(request, 'Este requerente ja terminou de efectuar o pago.')
        return redirect('pedido:listar_terminado')

class ListTerminadoView(LoginRequiredMixin, ListView):
	model = Pago
	template_name = 'terminado/list.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Listado de Projectos Terminados'
		return context

class UpdateTerminadoView(LoginRequiredMixin, UpdateView):
	model = Pago
	template_name = 'terminado/create.html'
	form_class = PagoForm
	success_url = reverse_lazy('pedido:listar_terminado')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Editar Pago'
		return context

class DetailTerminadoView(LoginRequiredMixin, DetailView):
    model = Pago
    template_name = 'terminado/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalhe do Projecto Terminado'
        return context

# Function Directivo
class ListDirectivoView(LoginRequiredMixin, ListView):
	model = Directivo
	template_name = 'directivo/list.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Directivo'
		return context

class UpdateDirectivoView(LoginRequiredMixin, UpdateView):
	model = Directivo
	template_name = 'directivo/create.html'
	form_class = DirectivoForm
	success_url = reverse_lazy('pedido:listar_directivo')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Editar Directivo'
		return context

class DeleteDirectivoView(LoginRequiredMixin, DeleteView):
	model = Directivo
	template_name = 'directivo/delete.html'
	success_url = reverse_lazy("pedido:listar_directivo")
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Directivo'
		return context

class CreateDirectivoView(LoginRequiredMixin, CreateView):
	model = Directivo
	template_name = 'directivo/create.html'
	form_class = DirectivoForm
	success_url = reverse_lazy('pedido:listar_directivo')
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Criar Director'
		return context

def pdf (request,pk):
	try:
		obj = get_object_or_404(Pago,pk=pk)
		ruta = ''

		if obj.recibo_primeiro.path:
			ruta = obj.recibo_primeiro.path

		elif obj.recibo_segundo.path:
			ruta = obj.recibo_segundo.path

		elif obj.recibo_terceiro.path:
			ruta = obj.recibo_terceiro.path

		elif obj.processo_requerente.path:
			ruta = obj.processo_requerente.path
		else:
			ruta = obj.parecer_tecnico.path
		print(ruta)

		with open(ruta, 'rb') as pdf:
			response = HttpResponse(pdf.read(),content_type='application/pdf')
			response['Content-Disposition'] = 'filename=some_file.pdf'
			return response
	except Exception as e:
		# messages.warning(request, 'Este documento não foi anexado.')
		print(e)
		return redirect('pedido:listar_terminado')


# Recibo de Inicialização da Legalização
class GenerarPDF(View):
	def link_callback(self,uri,rel):
		sUrl = settings.STATIC_URL
		sRoot= settings.STATIC_ROOT
		mUrl = settings.MEDIA_URL
		mRoot = settings.MEDIA_ROOT

		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot,uri.replace(sUrl, ""))
		else:
			return uri

		if not os.path.isfile(path):
			raise Exception(
				'media URl must start with %s or %s' %(sUrl,mUrl)
			)
		return path



	def get(self, request, *args, **kwargs):
		pk = self.kwargs.get('pk', 0)
		data = date.today()
		direct = Directivo.objects.last()



		requerent = obj = get_object_or_404(TerrenoLegalizar,pk=pk)
		template_path = 'reporte.html'
		meses_pt = ['Janeiro','Fevereiro','Março','Abril','Maio','Junio','Julio','Agosto','Setembro','Outubro','Novembro','Dezembro']
		meses_in = ['January','February','March','April','May','June','July','August','September','October','November','December']
		if data.strftime("%B") in meses_in:
			value_index = meses_in.index(data.strftime("%B"))
			mes = meses_pt[value_index]
		context= {
			'icon': '{}{}'.format(settings.STATIC_URL,'img/insigna.jpg'),
			'title': 'REPÚBLICA DE ANGOLA',
			'title_two': 'GOVERNO PROVINCIAL DO CUNENE',
			'title_three': 'ADMINISTRAÇÃO MUNICIPAL DE NAMACUNDE',
			'title_four': 'DIRECÇÃO MUNICIPAL DE INFRA-ESTRUCTURAS, ORDENAMENTO DO TERRITÓRIO E HABITAÇÃO',
			'title_five': f'TÍTULO DE CONFIRMAÇÃO DE ENTRADA DE PROCESSO Nº{requerent.pk}/{data.year}',

			'body': f'A Direcção Municipal Dos Serviços Técnicos, vem por este intermédio confirmar, para os devidos julgados convenientes, que a Empresa Lda Representada (o), pelo senhor {requerent.pessoaEmpresa.nome_requerente}, nascido aos {requerent.pessoaEmpresa.data_nascimento.day}/{requerent.pessoaEmpresa.data_nascimento.month}/{requerent.pessoaEmpresa.data_nascimento.year}, Filho(a) de {requerent.pessoaEmpresa.nome_pai} e de {requerent.pessoaEmpresa.nome_mae}, natural de {requerent.pessoaEmpresa.naturalidade}, Municipio de {requerent.pessoaEmpresa.data_nascimento.year}, Provincia do(a) {requerent.pessoaEmpresa.provincia} portador do B.I Nº {requerent.pessoaEmpresa.bi}, Passado pelo Arquivo de identificação Nacional de {requerent.pessoaEmpresa.passado_bi} e residente em {requerent.pessoaEmpresa.residencia} Rua(Avenida)_X_, Casa Nº {requerent.pessoaEmpresa.numero_casa}, Telefone Nº {requerent.pessoaEmpresa.telefone}.',
			'body_two': f'Procedeu a Entrada do Projecto de {requerent.projecto} que fica arquivado nesta Direção Municipal de Infra-Estructuras, Ordenamento do Território e Habitação de Namacunde, Provincia de {requerent.provincia_arquivacao}, sob processo Nº {requerent.pk}/{data.year} nos termos do disposto no Decreto nº80/06 no artigo 99º(Deposito legal de Projecto).',

			'body_three':f'O Projecto ora apresentado, é referente ao seu imóvel localizado no Talhão Nº__X__. Quarterão Nº19, Localidade(Bairro) X, Municipio do {requerent.municipio} / Província do {requerent.provincia_arquivacao}, Conforme o croquis de localização em anexo.',
			'body_four':f'Por ser verdade e me ter sido solicitado passsei o presente título de confirmação de entrada de processo, que vai ser por mim assinado e autenticado com o carimbo a óleo em uso nesta instituição.',
			'body_five':f'DIRECÇÃO MUNICIPAL DE INFRA-ESTRUCTURAS, ORDENAMENTO DO TERRITÓRIO E HABITAÇÃO em Namacunde, aos {data.day} de {mes} de {data.year}.',

			'director':f'{direct.nome_directivo}',
			'requerent':f'{requerent.pessoaEmpresa.nome_requerente}'
		}
		response = HttpResponse(content_type='application/pdf')
		# response['Content-Disposition'] = 'attachment; filename="contrato.pdf"'
		# find the template and render it.
		template = get_template(template_path)
		html = template.render(context)
		# create a pdf
		pisa_status = pisa.CreatePDF(
			html, dest=response,
			link_callback=self.link_callback
		)
		if pisa_status.err:
		   	return HttpResponse('Nós encontramos alguns erros <pre>' + html + '</pre>')
		return response