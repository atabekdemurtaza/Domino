from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    price = models.DecimalField(default=0, decimal_places=2)
    stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    made = models.CharField(max_length=250)
    color = models.ManyToManyField('Color', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Color(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
