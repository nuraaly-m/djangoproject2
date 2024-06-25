from django.shortcuts import render,get_object_or_404
from django.views import generic
from catalog.models import Review
from main_page.models import *
from . import forms


class GoodDetailView(generic.DetailView):
    template_name = 'catalog/catalog_detail.html'
    context_object_name = 'good'


    def get_object(self, **kwargs):
        good_id = self.kwargs.get('id')
        print(good_id)
        return get_object_or_404(Goods, id=good_id)


class CreateReviewView(generic.CreateView):
    template_name = 'catalog/create_review.html'
    form_class = forms.ReviewForm
    success_url = '/catalog/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)
