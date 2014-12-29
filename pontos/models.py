from django.db import models

# Create your models here.

class Registro(models.Model):

    user = models.ForeignKey('auth.user')
    registro = models.DateTimeField(auto_now_add = False, auto_now=False)
    # comprovante = models.FileField(upload_to=UPLOAD_DIR, max_length=100)
    criado_em = models.DateTimeField(auto_now_add = True, auto_now=False)
    alterado_em = models.DateTimeField(auto_now_add = False, auto_now=True)

    def save(self, *args, **kwargs):
        super(Registro, self).save(*args, **kwargs)

    def __unicode__(self):

        return "%s" % self.registro