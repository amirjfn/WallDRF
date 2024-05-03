from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('list', views.AdListView.as_view(), name='list'),
    path('create', views.AdCreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.AdDetailView.as_view(), name='detail'),
    path('search', views.AdSeaechView.as_view(), name='search'),
]