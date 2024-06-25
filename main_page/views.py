from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from main_page.models import Goods, Slogan, Videos


class GoodList(generic.ListView):
    template_name = "blog/goods_list.html"
    context_object_name = "goods"
    model = Goods
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slogans'] = Slogan.objects.order_by('-id')
        context['videos'] = Videos.objects.order_by('-id')
        return context
