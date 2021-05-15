from django.db import models

# Create your models here.
class  Realsimulation(models.Model):
      id = models.IntegerField(primary_key=True) 
      date = models.DateTimeField()
      open = models.FloatField(null=True,blank=True)
      high = models.FloatField(null=True,blank=True)
      low = models.FloatField(null=True,blank=True)
      close = models.FloatField(null=True,blank=True)
      volume = models.IntegerField(null=True,blank=True)
      currency = models.IntegerField(null=True,blank=True)
      code = models.CharField(max_length=255)
      rsi = models.FloatField(null=True,blank=True)
      days50 = models.FloatField(null=True,blank=True)
      days150 = models.FloatField(null=True,blank=True)
      days200 = models.FloatField(null=True,blank=True)
      weeks20 = models.FloatField(null=True,blank=True)
      stdev = models.FloatField(null=True,blank=True)
      bb = models.FloatField(null=True,blank=True)
      def __str__(self):
            return self.code

class Fandamental(models.Model):
      id = models.IntegerField() 
      meigara = models.CharField(max_length=255)
      code = models.CharField(max_length=255,primary_key=True)
      uriagetuuki1 = models.FloatField(null=True,blank=True)
      uriagetuuki2 = models.FloatField(null=True,blank=True)
      riekituuki1 = models.FloatField(null=True,blank=True)
      riekituuki2 = models.FloatField(null=True,blank=True)
      epstuuki1 = models.FloatField(null=True,blank=True)
      epstuuki2 = models.FloatField(null=True,blank=True)
      uriageshihanki1 =models.FloatField(null=True,blank=True)
      uriageshihanki2 =models.FloatField(null=True,blank=True)
      uriageshihanki3 =models.FloatField(null=True,blank=True)
      riekishihanki1 =models.FloatField(null=True,blank=True)
      riekishihanki2 =models.FloatField(null=True,blank=True)
      riekishihanki3 =models.FloatField(null=True,blank=True)
      epsshihanki1 =models.FloatField(null=True,blank=True)
      epsshihanki2 =models.FloatField(null=True,blank=True)
      epsshihanki3 =models.FloatField(null=True,blank=True)