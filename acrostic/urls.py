from django.urls import path

from . import views

app_name = 'acrostic'
urlpatterns = [
  path('', views.index, name='index'),
  path('poem/<int:acrostic_id>/', views.poem, name='poem'),
  path('create/', views.create, name='create'),
]
