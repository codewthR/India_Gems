from django.db import models

# Create your models here.



class state_about(models.Model):
    state_pics = models.ImageField(upload_to='imags')
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


# one to many relation 

class city_detail(models.Model):
    state_name = models.ForeignKey("state_about", on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)
    city_pics01 = models.ImageField(upload_to='city_pics')
    city_pics02 = models.ImageField(upload_to='city_pics')
    city_pics03 = models.ImageField(upload_to='city_pics')
    city_pics04 = models.ImageField(upload_to='city_pics')
    city_description = models.TextField() 


    def __str__(self):
        return self.city_name