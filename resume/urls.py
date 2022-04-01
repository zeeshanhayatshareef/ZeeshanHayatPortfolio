from django.urls import path
from resume import views

urlpatterns = [
    path('', views.Index, name='index'),
]
