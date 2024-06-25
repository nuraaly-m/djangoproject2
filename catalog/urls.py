from django.urls import path
from . import views


urlpatterns = [
    path('good/<int:id>/', views.GoodDetailView.as_view()),
    path('create_review/', views.CreateReviewView.as_view()),
]