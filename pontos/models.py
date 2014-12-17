from django.db import models

# Create your models here.

class Registro(models.Model):

    registro = models.DateTimeField(auto_now_add = False, auto_now=False)
    criado_em = models.DateTimeField(auto_now_add = True, auto_now=False)
    alterado_em = models.DateTimeField(auto_now_add = False, auto_now=True)
    imagem = models.CharField(max_length=120, default='no-image.jpg')


    def __unicode__(self):

        return "%s" % self.registro