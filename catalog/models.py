from django.db import models
from main_page.models import *


class Review(models.Model):
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,related_name='reviews')
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'