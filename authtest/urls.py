from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('<int:subject_id>/', views.detail, name='detail'),
    path('<int:subject_id>/update', views.update, name='update'),
    path('<int:subject_id>/delete', views.delete, name='delete'),
    path('<int:subject_id>/quiz', views.quiz, name='quiz'),
]