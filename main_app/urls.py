from django.urls import path
from . import views

urlpatterns = [
  # General Paths
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  # Quotes Paths
  path('quotes/', views.quotes_index, name='index'),
  path('quotes/<int:quote_id>/', views.quotes_detail, name='detail'),
  path('quotes/create/', views.QuoteCreate.as_view(), name='quotes_create'),
  path('quotes/<int:pk>/update/', views.QuoteUpdate.as_view(), name='quotes_update'),
  path('quotes/<int:pk>/delete/', views.QuoteDelete.as_view(), name='quotes_delete'),

  # Discussion Paths
  path('quotes/<int:quote_id>/add_discussion', views.add_discussion, name='add_discussion'),
  
  # Tags Paths
  path('quotes/<int:quote_id>/add_tag/<int:tag_id>/', views.add_tag, name='add_tag'),
  path('quotes/<int:quote_id>/remove_tag/<int:tag_id>/', views.remove_tag, name='remove_tag'),
  path('tags/', views.TagList.as_view(), name='tags_index'),
  path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
  path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
  path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
  path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),

  # Auth Paths
  path('accounts/signup/', views.signup, name='signup'),

]


