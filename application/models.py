from django.db import models


# Create your models here.
class Corpus(models.Model):
    txt = models.CharField(max_length=512)



chaise = Corpus.objects.create(txt = "Chaise")
table = Corpus.objects.create(txt = "Table")

 
  


    