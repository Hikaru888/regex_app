from django.urls import path
from . import views

app_name = 'regex_app'

urlpatterns = [
    path('confirm/', views.confirm, name='confirm'),
    path("", views.index, name="index"),
]