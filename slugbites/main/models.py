from django.db import models

# Create your models here.
class foodItem(models.Model):
    name = models.CharField(max_length=200)
    veggie = models.BooleanField()
    soy = models.BooleanField()
    eggs = models.BooleanField()
    milk = models.BooleanField()
    vegan = models.BooleanField()
    gluten = models.BooleanField() # True means gluten free
    halal = models.BooleanField()
    unknown = models.BooleanField()
    time = models.BooleanField()
    
    def __str__(self):
        return self.name()