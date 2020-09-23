from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

# Create your models here.
class Provincia(models.Model):
    Provincia_choice = (
        ('Cunene', 'Cunene'),
    )
    provincia = models.CharField(
        max_length=10, choices=Provincia_choice, unique=True)

    def __str__(self):
        return self.provincia

class Municipio(models.Model):
    Municipio_choice = (
        ('Namacunde', 'Namacunde'),
    )
    municipio = models.CharField(max_length=12, choices=Municipio_choice, unique=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.municipio

class Comuna(models.Model):
    Comuna_choice = (
        ('Namacunde', 'Namacunde'),
        ('Chiede', 'Chiede'),
    )
    comuna = models.CharField(max_length=20, choices=Comuna_choice, unique=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.comuna

class PessoaEmpresa(models.Model):
    ESTADO_CIVIL = (
        ('Solteiro','Solteiro'),
        ('Casado', 'Casado'),
        ('Divorciado','Divorciado'),
    )
    # Somente uma pessoa
    nome_requerente = models.CharField(verbose_name="Requerente",null = True,blank=True,max_length=50)
    empresa = models.CharField(verbose_name="Representado por",null=True,blank = True,max_length=70)
    data_nascimento = models.DateField(verbose_name="Data de nascimento",null = True,blank = True)
    nome_pai = models.CharField(verbose_name="Nome do Pai",max_length=100,null = True,blank = True)
    nome_mae = models.CharField(verbose_name="Nome da mãe",max_length=100,null = True,blank = True)
    estado_civil = models.CharField(max_length=18,verbose_name='Estado Civil',choices = ESTADO_CIVIL)
    naturalidade = models.CharField(verbose_name="Naturalidade",max_length=50,null = True,blank = True)
    bi = models.CharField(verbose_name="BI Nº",max_length=14,null = True,blank = True, unique=True)
    copia_de_bi = models.FileField(verbose_name="Cópia do BI'Só em formato PDF ou jpg'",upload_to='%y/%m/%d',null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg'])])
    passado_bi = models.CharField(verbose_name="Local de emissão",max_length=50,null=True, blank=True)
    comuna = models.ForeignKey(to = 'Comuna',on_delete=models.CASCADE,null=True,blank= True)
    municipio = models.ForeignKey(to = 'Municipio',on_delete=models.CASCADE,null=True,blank= True)
    provincia = models.ForeignKey(to = 'Provincia',on_delete=models.CASCADE,null=True,blank= True)
    residencia = models.CharField(verbose_name='Residençia',max_length=50,null=True,blank = True)
    numero_casa = models.PositiveIntegerField(verbose_name='Número da Casa',null=True,blank = True)
    sede = models.CharField(max_length=100,verbose_name='Localização da Sede da Empresa', null=True,blank=True)
    # Comúm
    email = models.EmailField(verbose_name="Email",null=True,blank=True)
    telefone = models.CharField(verbose_name='Nº de Telefone',null=True,blank = True,max_length=12, unique=True)

    def __str__(self):
        if self.empresa is None:
            return self.nome_requerente
        else:
            return f"{self.empresa}"

class TerrenoLegalizar(models.Model):
    projecto = models.CharField(verbose_name="Nome do projecto",max_length=255)
    localizacao = models.CharField(verbose_name = "Local do projecto",max_length=100)
    provincia_arquivacao = models.ForeignKey(to="Provincia",verbose_name="Provincia de arquivação",on_delete=models.CASCADE,max_length=100)
    quarterao = models.CharField(verbose_name="Quarteirão",max_length=100)
    comuna = models.ForeignKey(to = "Comuna", on_delete=models.CASCADE,verbose_name = "Localidade/Bairro",blank= True,null = True)
    municipio = models.ForeignKey(to='Municipio',on_delete=models.CASCADE,verbose_name = "Municipio",blank= True)
    data_entrada = models.DateField(auto_now_add=True)
    pessoaEmpresa = models.ForeignKey(to="PessoaEmpresa",on_delete=models.CASCADE,verbose_name ="Legalizador")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    pago_apreciado = models.DecimalField(verbose_name="Pagamento de Preciação", max_digits=6, decimal_places=2)
    metros = models.PositiveIntegerField(verbose_name="Extenção em metros quadrados",null=True,blank=True)

    def __str__(self):
        return self.projecto

class Pago(models.Model):
    parecer_tecnico = models.FileField(verbose_name="Parecer Técnico 'OBS: Só formato PDF'",upload_to='%y/%m/%d',validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null = True, blank = True)
    primeiro = models.FloatField(verbose_name = "Primeira prestação")
    recibo_primeiro = models.FileField(verbose_name="Recibo de deposito 'OBS: Solo formato PDF ou jpg'",upload_to='%y/%m/%d',validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg'])])
    segundo = models.FloatField(verbose_name="Segunda Prestação",default=0.00)
    recibo_segundo = models.FileField(verbose_name="Só formato PDF ou jpg",upload_to='%y/%m/%d',validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg'])],null = True, blank = True)
    terceiro = models.FloatField(verbose_name="Terceira e última prestação",default=0.00)
    recibo_terceiro = models.FileField(verbose_name="Só formato PDF ou jpg",validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg'])],upload_to='%y/%m/%d',null = True, blank = True)
    projecto_legalizado = models.OneToOneField(to="TerrenoLegalizar",on_delete=models.CASCADE,verbose_name='Projecto Legalizado')
    processo_requerente = models.FileField(verbose_name="Processo do Requerente 'OBS: Só em formato PDF'",upload_to='%y/%m/%d',validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null = True, blank = True)

    def __str__(self):
        if self.primeiro and self.segundo and self.terceiro:
            return str(3)
        elif self.primeiro and self.segundo:
            return str(2)
        else:
            return str(1)

class Directivo(models.Model):
    nome_directivo = models.CharField(max_length=100,verbose_name='Nome do Chefe de Secção')
    data_nascimento = models.DateField(verbose_name='Data de Nacimento')
    empossamento = models.DateField(verbose_name='Data de Empossamento')
    entrega_cargo = models.DateField(verbose_name='Data de Entrega do Cargo')
    copia_bi = models.FileField(verbose_name="'OBS: Só em formato PDF'",upload_to='%y/%m/%d',validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg'])],null = True, blank = True)

    def __str__(self):
        return self.nome_directivo