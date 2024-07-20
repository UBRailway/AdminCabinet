from pyclbr import Class
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='Url')
    job= models.CharField(max_length=50, blank=True, null=True, verbase_name="Должность")
    area=models.CharField(max_length=50, blank=True, null=True, verbase_name="Участок")
    station= models.CharField(max_length=50, blank=True, null=True, verbase_name='Станция')
    phone_number= models.CharField(max_length=50,blank=True, null=True, verbase_name="Номер телефона")
    mail= models.CharField(max_length=50, unique=True, blank=True, null=True, verbase_name="Эл.почта")
    image= models.ImageField(upload_to='main.images',blank=True, null=True, verbase_name="Изображение")
    access_level= models.CharField(max_length=15,blank=True, null=True, verbose_name='Уровень доступа' )

    class Meta: 
        db_table= 'Users'
        verbose_name = "Пользователь"
        verbose_name_plural= "Пользователи"


