from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('quotes/', views.quotes_index, name='index'),
  path('quotes/<int:quote_id>/', views.quotes_detail, name='detail')
]


