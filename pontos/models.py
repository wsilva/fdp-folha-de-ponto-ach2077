from django.db import models

# Create your models here.

class SpotHit(models.Model):

    user = models.ForeignKey('auth.user')
    spothit_datetime = models.DateTimeField(auto_now_add = False, auto_now=False)
    labor_day = models.ForeignKey(LaborDay)
    created_at = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now=True)
    ip_address = models.CharField(max_length=120, default='0.0.0.0')


    def save(self, *args, **kwargs):
        super(SpotHit, self).save(*args, **kwargs)

    def __unicode__(self):

        return "%s" % self.spothit_datetime

class LaborDay(models.Model):
    spothit_date = models.DateTime(auto_now_add = False, auto_now=False)

