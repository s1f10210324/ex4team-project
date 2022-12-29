from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('<int:folder_id>/', views.detail, name='detail'),
    path('<int:folder_id>/update', views.update, name='update'),
    path('<int:folder_id>/delete', views.delete, name='delete'),
    path('paper', views.card, name='paper'),
    path('paper', views.paperhtml, name='paperhtml'),
    path('<int:card_id>/paper_detail', views.paper_detail, name='paper_detail'),
    path('<int:card_id>/paper_delete', views.paper_delete, name='paper_delete'),
]