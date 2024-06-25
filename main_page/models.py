from django.db import models

class Slogan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name='название товара')
    image = models.ImageField(upload_to='goods/', verbose_name='загрузите фото')
    price = models.PositiveIntegerField(verbose_name='price')
    video = models.ForeignKey('Videos',on_delete=models.CASCADE,related_name='goods')


    def __str__(self):
        return f'{self.name}--{self.price}'


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Videos(models.Model):
    video = models.URLField(verbose_name='video')

    def __str__(self):
        return f'{self.video}'
