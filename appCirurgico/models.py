from django.db import models

# Create your models here.
class FundaoCirurgicoTB(models.Model):
    text        = models.CharField(max_length=255)
    subtext     = models.CharField(max_length=255)
    author      = models.CharField(max_length=255)
    processed   = models.BooleanField(default=False)
    date        = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.text}, {self.author}"