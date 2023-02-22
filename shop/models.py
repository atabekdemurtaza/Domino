#имортированные мобулей
from django.db import models
from ckeditor import fields
from django.contrib.auth.models import AbstractUser


#бд пользователя
class CustomUser(AbstractUser):
     CITY = (
          ('NKS', 'Нукус'),
          ('TASH', 'Ташкент'),
     )

     first_name = models.CharField('Имя*', max_length=512)
     last_name = models.CharField('Фамилия*', max_length=512)
     email = models.EmailField('Эл.почта*')

     city = models.CharField('Город*', choices=CITY, max_length=512)

     phone = models.CharField('Телефон*', max_length=75)


     def __str__(self) -> str:
          return self.username
     
     class Meta:
          verbose_name = 'Покупатель'
          verbose_name_plural = 'Покупатели'


"""----------------------------------------------------------------------"""
#бд продукта
class Product(models.Model):
     COUNTRY = (
          ('TURC', 'Турция'),
          ('UZB', 'Узбексиатн'),
          ('CHIN', 'Китай'),
          ('USA', 'США')
     )

     name = models.CharField('Наименование*', max_length=250)
     desc = fields.RichTextField('Описание*')

     main_img = models.ImageField('Главное фото*', upload_to='images/')
     image1 = models.ImageField('Фотография 1', upload_to='images/', blank=True, null=True)
     image2 = models.ImageField('Фотография 2', upload_to='images/', blank=True, null=True)
     image3 = models.ImageField('Фотография 3', upload_to='images/', blank=True, null=True)

     price = models.DecimalField('Ценник*', default=0, decimal_places=2, max_digits=100000000)
     stock = models.BooleanField('Наличие*', default=True)

     made = models.CharField('Изготовление*', max_length=512, choices=COUNTRY)

     category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория*')
     size = models.ManyToManyField('Size', verbose_name='Размер*')
     color = models.ManyToManyField('Color', verbose_name='Цвет*')  

     brand = models.CharField('Бренд*', max_length=250)


     def __str__(self):
          return self

     class Meta:
          verbose_name = 'Товар'
          verbose_name_plural = 'Товары'
"""----------------------------------------------------------------------"""


#бд категорий
class Category(models.Model):
    name = models.CharField('Название*', max_length=250)
    image = models.ImageField('Картинка*', upload_to='categoryImg/')
    desc = fields.RichTextField('Описание*')
    

    def __str__(self):
          return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

        
#бд цветов
class Color(models.Model):
     name = models.CharField('Название*', max_length=250)
    

     def __str__(self):
          return self.name

     class Meta:
          verbose_name = 'Цвет'
          verbose_name_plural = 'Цвета'


#бд размеров
class Size(models.Model):
     name = models.CharField('Название*', max_length=250)
    

     def __str__(self):
          return self.name

     class Meta:
          verbose_name = 'Размер'
          verbose_name_plural = 'Размеры'

