import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from datetime import date
from django.http import Http404
from .models import *

# Create your views here.
def consulta_print(request, pk=None):
    try:
        terreno = TerrenoLegalizar.objects.get(id=pk)
        director = Directivo.objects.last()
    except ValueError:
        raise Http404()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=reporte.pdf'
    buffer = BytesIO()
    #Creamos el objeto PDF, usando el objeto BytesIO como si fuera un "archivo".
    p = canvas.Canvas(buffer, pagesize=A4)
    fecha = date.today()
    p.setTitle('Contrato')
    p.translate(cm,cm)
    p.drawImage("./static/img/insigna.jpg", 220, 700, width=70, height=85)
    p.setFont('Helvetica',12)
    #Header
    p.drawString(185, 679,"REPUBLICA DE ANGOLA")
    p.drawString(145, 660,"GOVERNO DA PROVINCIA DE CUNENE")
    p.drawString(120, 641,"ADMINISTRAÇÃO MUNICIPAL  DE NAMACUNDE")
    p.drawString(110, 622,"DIRECÇÃO MUNICIPAL DOS SERVIÇOS TÉCNICOS")
    #Body
    p.setFont('Helvetica',12)
    p.drawString(60,570,f"TÍTULO DE CONFIRMAÇÃO DE ENTRADA DE PROCESSO Nº{terreno.pk}/{fecha.year}")
    p.drawString(10,540,f"A Direcção Municipal dos Serviços Técnicos, vem por este intermédio confirmar, para os devidos")
    p.drawString(10,520,f"julgados convenientes, Que o senhor {terreno.pessoaEmpresa.nome_requerente}, {terreno.pessoaEmpresa.estado_civil}, nascido aos")
    p.drawString(10,500,f"{terreno.pessoaEmpresa.data_nascimento.day}/{terreno.pessoaEmpresa.data_nascimento.month}/{terreno.pessoaEmpresa.data_nascimento.year}, Filho(a) de {terreno.pessoaEmpresa.nome_pai} e de {terreno.pessoaEmpresa.nome_mae},comuna de {terreno.pessoaEmpresa.comuna}, Municipio de {terreno.pessoaEmpresa.municipio},")

    p.drawString(10,480,f"província de {terreno.pessoaEmpresa.provincia}, portador do B.I Nº {terreno.pessoaEmpresa.bi}, Passado pelo Arquivo de identificação")

    p.drawString(10,460,f"Nacional de {terreno.pessoaEmpresa.passado_bi} e residente em {terreno.pessoaEmpresa.municipio}, Rua(avenida) {terreno.pessoaEmpresa.residencia}, Casa Nº {terreno.pessoaEmpresa.numero_casa},")
    p.drawString(10,440, f"Telefone {terreno.pessoaEmpresa.telefone}.")

    p.drawString(10,400,f"Procedeu a Entrada do seu Projecto de Construção  de um (a) {terreno.projecto} que fica")
    p.drawString(10,380,f"arquivado nesta Direcção Municipal dos Serviços Técnicos de {terreno.municipio}, Província do {terreno.provincia_arquivacao}, sob")
    p.drawString(10,360,f"processo Nº{terreno.pk}/{fecha.year} nos termos do disposto no Decreto nº80/06 no artigo 99º (Deposito legal do")
    p.drawString(10,340,f"Projecto).")



    p.drawString(10,300,f"O Projecto ora apresentado, é referente ao seu imóvel localizado no Talhão Nº__X__.")
    p.drawString(10,280,f"Quarterão Nº{terreno.quarterao}, Localidade(Bairro) X, Municipio do {terreno.municipio} / Província do {terreno.provincia_arquivacao},")
    p.drawString(10,260,f"Conforme o croquis de localização em anexo.")

    p.drawString(10,230,f"Por ser verdade e me ter sido solicitado passsei o presente título de confirmação de entrada ")
    p.drawString(10,210,f"de processo, que vai ser por mim assinado e autenticado com o carimbo a óleo em uso nesta")
    p.drawString(10,190,f"instituição.")
    p.drawString(40,140,f"Direcção Municipal dos Serviços Técnicos em Namacunde, aos {fecha.day} de {fecha.month} de {fecha.year}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(70,70,"A CHEFE DE SECÇÃO                                                O DEPOSITANTE    ")
    p.drawString(40,46,".............................................................                           .................................................")
    p.drawString(65,26,f"{director}                                {terreno.pessoaEmpresa.nome_requerente}")

    #Cerramos limpiamente el objeto PDF.
    p.showPage()
    # salvamos el pdf
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response