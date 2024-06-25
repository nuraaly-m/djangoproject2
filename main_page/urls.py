from django.urls import path
from . import views


urlpatterns = [
    path('goods/', views.GoodList.as_view()),
]