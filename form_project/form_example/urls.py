from django.urls import path
from . import views

urlpatterns = [
    path('form_example/', views.form_example, name="form_example"),
]